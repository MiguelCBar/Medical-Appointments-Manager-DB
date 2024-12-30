#!/usr/bin/python3
# Copyright (c) BDist Development Team
# Distributed under the terms of the Modified BSD License.
import os
from logging.config import dictConfig

import re
from datetime import datetime, timedelta

from flask import Flask, jsonify, request
from psycopg.rows import namedtuple_row
from psycopg_pool import ConnectionPool

# Use the DATABASE_URL environment variable if it exists, otherwise use the default.
# Use the format postgres://username:password@hostname/database_name to connect to the database.
DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://saude:Saude@postgres/saude")

pool = ConnectionPool(
    conninfo=DATABASE_URL,
    kwargs={
        "autocommit": True,  # If True don’t start transactions automatically.
        "row_factory": namedtuple_row,
    },
    min_size=4,
    max_size=10,
    open=True,
    # check=ConnectionPool.check_connection,
    name="postgres_pool",
    timeout=5,
)

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s:%(lineno)s - %(funcName)20s(): %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

app = Flask(__name__)
app.config.from_prefixed_env()
log = app.logger


        
@app.route("/", methods=("GET",))
def lista_clinicas():
    """Lista todas as clinicas (nome e morada)."""

    with pool.connection() as conn:
        with conn.cursor() as cur:

            clinicas = cur.execute(
                """
                SELECT nome, morada
                FROM clinica;
                """,
                {},
            ).fetchall()

            if not clinicas:  # Verifica se a lista de clínicas está vazia
                return jsonify({"message": "Não existem clínicas no Sistema.", "status": "error"}), 404
            
            log.debug(f"Found {cur.rowcount} rows.")

    return jsonify(clinicas), 200


@app.route("/c/<clinica>/", methods=("GET",))
def lista_especialidades_clinica(clinica):
    """Lista todas as especialidades oferecidas na <clinica>."""

    with pool.connection() as conn:
        with conn.cursor() as cur:

            clinica_procura = cur.execute(
                """
                SELECT *
                FROM clinica
                WHERE nome = %(clinica)s;
                """,
                {"clinica": clinica}
            ).fetchone()

            if not clinica_procura:
                return jsonify({"message": "Clínica não existe no Sistema.", "status": "error"}), 404

            especialidades = cur.execute(
                """
                SELECT DISTINCT m.especialidade
                FROM medico m
                JOIN trabalha t ON m.nif = t.nif
                WHERE t.nome = %(clinica)s;
                """,
                {"clinica": clinica},
            ).fetchall()

            if not especialidades:
                return jsonify({"message": "Não existem médicos colocados nesta clínica.", "status": "error"}), 404

            log.debug(f"Found {cur.rowcount} rows.")

    return jsonify(especialidades), 200


@app.route("/c/<clinica>/<especialidade>/", methods=("GET",))
def lista_medico_especialidade_horario(clinica, especialidade):
    """Lista todos os médicos (nome) da <especialidade> que
    trabalham na <clínica> e os primeiros três horários
    disponíveis para consulta de cada 1 um deles (data e hora)."""

    with pool.connection() as conn:
        with conn.cursor() as cur:

            clinica_procura = cur.execute(
                """
                SELECT nome
                FROM clinica
                WHERE nome = %(clinica)s;
                """,
                {"clinica": clinica}
            ).fetchone()

            if not clinica_procura:
                return jsonify({"message": "Clínica não existe no Sistema", "status": "error"}), 404

            especialidade_procura = cur.execute(
                """
                SELECT DISTINCT m.especialidade
                FROM medico m
                JOIN trabalha t ON m.nif = t.nif
                WHERE t.nome = %(clinica)s AND m.especialidade = %(especialidade)s;
                """,
                {"clinica": clinica, "especialidade": especialidade},
            ).fetchall()

            if not especialidade_procura:
                return jsonify({"message": "A especialidade não existe na Clínica.", "status": "error"}), 404

            medicos_consultas_hora = cur.execute(
                """
                WITH medicos_especialidade_clinica AS (
                SELECT m.nome AS nome_medico, m.nif as medico_nif, t.dia_da_semana as dia_da_semana
                FROM medico m
                JOIN trabalha t on m.nif = t.nif
                WHERE m.especialidade = %(especialidade)s AND t.nome = %(clinica)s
                ),
                    horarios_disponiveis AS (
                SELECT mec.nome_medico, mec.medico_nif, h.data, h.hora
                FROM medicos_especialidade_clinica mec
                CROSS JOIN Horarios h
                LEFT JOIN consulta c ON mec.medico_nif = c.nif AND h.data = c.data AND h.hora = c.hora
                WHERE c.id IS NULL AND (h.data + h.hora) > CURRENT_TIMESTAMP + interval '1 hour' 
                    AND EXTRACT(DOW FROM h.data) - 1 = mec.dia_da_semana
                )
                SELECT hd.nome_medico, hd.medico_nif, TO_CHAR(hd.data, 'YYYY-MM-DD') AS data, hd.hora
                FROM horarios_disponiveis hd
                GROUP BY hd.nome_medico, hd.medico_nif, hd.data, hd.hora;
                """,
                {"clinica": clinica, "especialidade": especialidade},
            ).fetchall()

            if not medicos_consultas_hora:
                return jsonify({"message": "Não existem horários disponíveis.", "status": "error"}), 404

            log.debug(f"Found {cur.rowcount} rows.")
            medicos_agrupados = {}
            for row in medicos_consultas_hora:
                medico = row[0]
                nif = row[1]
                if medico not in medicos_agrupados:
                    medicos_agrupados[medico] = {"nif": nif, "horarios": []}
                if len(medicos_agrupados[medico]["horarios"]) < 3:
                    medicos_agrupados[medico]["horarios"].append({"data": row[2], "hora": str(row[3])})
                    
    return jsonify(medicos_agrupados), 200



def validar_ssn(ssn):
    # Verifica se o SSN contém apenas dígitos e tem 11 caracteres
    return bool(re.match(r'^\d{11}$', ssn))

def validar_nif(nif):
    
    # Verifica se o NIF contém apenas dígitos e tem 9 caracteres
    return bool(re.match(r'^\d{9}$', nif))


def validar_data_hora(data, hora):
    
    try:
        # Tenta criar um objeto datetime a partir da string de data
        data_hora = datetime.strptime(data + " " + hora, "%Y-%m-%d %H:%M")
        
        # Verifica se o horário está dentro do intervalo permitido (8-13h e 14-19h)
        if not ((data_hora.hour >= 8 and data_hora.hour < 13) or (data_hora.hour >= 14 and data_hora.hour < 19)):
            return "Horário de consulta deve ser entre 8h e 13h ou entre 14h e 19h."
        
        # Verifica se o minuto da hora é exatamente 0 ou 30
        if data_hora.minute not in [0, 30]:
            return "Hora exata ou meia-hora necessária para fazer o registro."
        
        # Verifica se a data e hora estão no futuro (com pelo menos 1 hora de antecedência)
        if data_hora < (datetime.now() + timedelta(hours=1)):
            return "Impossível registrar uma consulta com data e hora desatualizadas."
        
        return None
    except ValueError:
        return "Formato de data e hora inválido (Data: YYYY-MM-DD e Hora: HH:MM)"


@app.route("/a/<clinica>/registar/", methods=("POST",))
def marca_consulta(clinica):
    """Registra uma marcação de consulta na <clinica> na base
        de dados (populando a respectiva tabela). Recebe como
        argumentos um paciente, um médico, e uma data e hora
        (posteriores ao momento de agendamento)."""

    paciente_ssn = request.args.get("paciente")
    medico_nif = request.args.get("medico")
    data = request.args.get("data")
    hora = request.args.get("hora")

    error = None

    if not all([paciente_ssn, medico_nif, data, hora]):
        error = "Preencha todos os campos."
    else:
        if not validar_ssn(paciente_ssn):
            error = "Código ssn do paciente inválido."
        elif not validar_nif(medico_nif):
            error = "Código nif do médico inválido."
        else:
            error = validar_data_hora(data, hora)
    
    if error is not None:
        return jsonify({"message": error, "status": "error"}), 400

    with pool.connection() as conn:
        with conn.cursor() as cur:
            clinica_procura = cur.execute(
                """
                SELECT nome
                FROM clinica
                WHERE nome = %(clinica)s;
                """,
                {"clinica": clinica}
            ).fetchone()
            if not clinica_procura:
                return jsonify({"message": "Clínica não existe no Sistema", "status": "error"}), 404

            
            medico_existente = cur.execute(
                """
                SELECT COUNT(*)
                FROM medico
                WHERE nif = %(medico_nif)s;
                """,
                {"medico_nif": medico_nif},
            ).fetchone()[0]
            if medico_existente == 0:
                return jsonify({"message": "Médico não existe no sistema.", "status": "error"}), 404

            consultas_medico_count = cur.execute(
                """
                SELECT COUNT(*)
                FROM consulta
                WHERE nif = %(medico_nif)s AND data = %(data)s AND hora = %(hora)s;
                """,
                {"medico_nif": medico_nif, "data": data, "hora": hora},
            ).fetchone()[0]
            if consultas_medico_count != 0:
                return jsonify({"message": "Medico ocupado neste horário.", "status": "error"}), 404  
            paciente_existente = cur.execute(
                """
                SELECT COUNT(*)
                FROM paciente
                WHERE ssn = %(paciente_ssn)s;
                """,
                {"paciente_ssn": paciente_ssn},
            ).fetchone()[0]
            if paciente_existente == 0:
                return jsonify({"message": "Paciente não existe no sistema.", "status": "error"}), 404

            paciente_consulta_count = cur.execute(
                """
                SELECT COUNT(*)
                FROM consulta
                WHERE ssn = %(paciente_ssn)s AND data = %(data)s AND hora = %(hora)s;
                """,
                {"paciente_ssn": paciente_ssn, "data": data, "hora": hora},
            ).fetchone()[0]
            if paciente_consulta_count != 0:
                return jsonify({"message": "Paciente já registou uma consulta neste horário.", "status": "error"}), 404
 
            dia_da_sem = datetime.strptime(data, '%Y-%m-%d').weekday()

            clinica_nome = cur.execute(
                """
                SELECT nome
                FROM trabalha
                WHERE nif = %(medico_nif)s AND dia_da_semana = %(dia_da_sem)s;
                """,
                {"medico_nif": medico_nif, "dia_da_sem": dia_da_sem},
            ).fetchone()
            if clinica_nome is None or clinica_nome[0] != clinica:
                return jsonify({"message": "O médico não trabalha nesta clínica neste dia.", "status": "error"}), 404

            cur.execute(
                """
                INSERT INTO consulta ( ssn, nif, nome, data, hora, codigo_sns)
                VALUES ( %(paciente_ssn)s, %(medico_nif)s, %(clinica)s, %(data)s, %(hora)s, NULL);
                """,
                {"paciente_ssn": paciente_ssn, "medico_nif": medico_nif, "clinica": clinica, "data": data, "hora": hora},
            )

            log.debug(f"Registered {cur.rowcount} rows.")

    return jsonify("Registo com sucesso."), 200


@app.route("/a/<clinica>/cancelar/", methods=("POST",))
def cancela_consulta(clinica):
    """Cancela uma marcação de consulta que ainda não se realizou
        na <clinica> (o seu horário é posterior ao momento do
        cancelamento), removendo a entrada da respectiva tabela na
        base de dados. Recebe como argumentos um paciente, um
        médico, e uma data e hora."""
    
    paciente_ssn = request.args.get("paciente")
    medico_nif = request.args.get("medico")
    data = request.args.get("data")
    hora = request.args.get("hora")

    error = None

    if not all([paciente_ssn, medico_nif, data, hora]):
        error = "Preencha todos os campos."
    else:
        if not validar_ssn(paciente_ssn):
            error = "Código ssn do paciente inválido."
        if not validar_nif(medico_nif):
            error = "Código nif do médico inválido."
        error = validar_data_hora(data, hora)
    
    if error is not None:
        return jsonify({"message": error, "status": "error"}), 400
    
    with pool.connection() as conn:
        with conn.cursor() as cur:
            try:
                clinica_procura = cur.execute(
                    """
                    SELECT nome
                    FROM clinica
                    WHERE nome = %(clinica)s;
                    """,
                    {"clinica": clinica}
                ).fetchone()
                if not clinica_procura:
                    return jsonify({"message": "Clínica não existe no Sistema", "status": "error"}), 404
                    
                paciente_existente = cur.execute(
                    """
                    SELECT COUNT(*)
                    FROM paciente
                    WHERE ssn = %(paciente_ssn)s;
                    """,
                    {"paciente_ssn": paciente_ssn},
                ).fetchone()[0]
                if paciente_existente == 0:
                    return jsonify({"message": "Paciente não existe no sistema.", "status": "error"}), 404
                    
                consultas_count = cur.execute(
                    """
                    SELECT COUNT(*)
                    FROM consulta
                    WHERE nif = %(medico_nif)s AND ssn = %(paciente_ssn)s AND data = %(data)s AND hora = %(hora)s;
                    """,
                    {"medico_nif": medico_nif, "paciente_ssn": paciente_ssn, "data": data, "hora": hora},
                ).fetchone()[0]
                if consultas_count == 0:
                    return jsonify({"message": "Consulta não existe.", "status": "error"}), 404

                dia_da_sem = datetime.strptime(data, '%Y-%m-%d').weekday() 
                clinica_nome = cur.execute(
                    """
                    SELECT nome
                    FROM trabalha
                    WHERE nif = %(medico_nif)s AND dia_da_semana = %(dia_da_sem)s;
                    """,
                    {"medico_nif": medico_nif, "dia_da_sem": dia_da_sem},
                ).fetchone()
                if clinica_nome is None:
                    return jsonify({"message": "O médico não trabalha nesta clínica neste dia.", "status": "error"}), 404

                cur.execute(
                    """
                    DELETE FROM consulta
                    WHERE ssn = %(paciente_ssn)s AND nif = %(medico_nif)s AND data = %(data)s AND hora = %(hora)s;
                    """,
                    {"paciente_ssn": paciente_ssn, "medico_nif": medico_nif, "data": data, "hora": hora},
                )
            except Exception as e:
                return jsonify({"message": "Não foi possível cancelar a consulta.", "status": "error"}), 500
                
            else:
                log.debug(f"Deleted {cur.rowcount} rows.")

    return jsonify("Cancelou a consulta com sucesso."), 200

if __name__ == "__main__":
    app.run()
