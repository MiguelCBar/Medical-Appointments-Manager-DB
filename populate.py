import random
import calendar
import copy
from datetime import datetime
"""----------------------------------Listas-----------------------------------------"""
dias_no_mes_23 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dias_no_mes_24 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]



all_nomes = [
    "Ana", "Beatriz", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
    "Kleber", "Larissa", "Marcos", "Natália", "Otávio", "Patrícia", "Quintino", "Raquel", "Sérgio", "Tatiana",
    "Ursula", "Vinícius", "Wagner", "Ximena", "Yara", "Zeca", "Alex", "Bruno", "Camila", "Diego",
    "Elaine", "Felipe", "Giovana", "Hugo", "Isabela", "João", "Karen", "Lucas", "Marta", "Nicolas",
    "Olívia", "Pedro", "Quésia", "Renato", "Simone", "Tiago", "Ulisses", "Vanessa", "William", "Xavier",
    "Yuri", "Zélia", "Amanda", "Bernardo", "Cecília", "Davi", "Esther", "Fernando", "Gustavo", "Heloísa",
    "Iara", "Júlio", "Kátia", "Luís", "Marina", "Natanael", "Orlando", "Paula", "Quirino", "Rebeca",
    "Samuel", "Tânia", "Ubirajara", "Vera", "Wallace", "Xena", "Yasmin", "Zion", "Aline", "Brenda",
    "Cláudio", "Diogo", "Elisa", "Frederico", "Gabriela", "Henrique", "Ivo", "Janaína", "Kauê", "Lúcia",
    "Matheus", "Neuza", "Otília", "Paulo", "Quintina", "Ricardo", "Sofia", "Thales", "Uriel", "Vítor",
    "Wesley", "Xuxa", "Yolanda", "Zara", "Alberto", "Bianca", "Caio", "Denise", "Emanuel", "Fátima",
    "Guilherme", "Heitor", "Inês", "Jorge", "Kelly", "Luan", "Maurício", "Nathália", "Osvaldo", "Pâmela",
    "Quitéria", "Roberto", "Suzana", "Túlio", "Valéria", "Wellington", "Xandão", "Yuri", "Zuleica",
    "Adriana", "Brás", "Célia", "Dorival", "Eduarda", "Fabiano", "Geovana", "Hélio", "Ivana", "Julio",
    "Karina", "Lia", "Max", "Norma", "Osmar", "Priscila", "Rodrigo", "Silvia", "Tatiane", "Ugo",
    "Vanda", "Waldemar", "Ximena", "Ygor", "Zenaide", "André", "Bárbara", "Catarina", "Evelyn", "Flávio",
    "Graciela", "Ícaro"
]

all_apelidos = [
    "Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Almeida", "Costa", "Pereira", "Gomes",
    "Martins", "Araújo", "Melo", "Barbosa", "Ribeiro", "Alves", "Cardoso", "Schmidt", "Rocha", "Dias",
    "Correia", "Ramos", "Teixeira", "Carvalho", "Nunes", "Castro", "Moreira", "Lima", "Machado", "Lopes",
    "Freitas", "Vieira", "Monteiro", "Mendes", "Nogueira", "Pinto", "Reis", "Andrade", "Gonçalves", "Fernandes",
    "Cavalcanti", "Moraes", "Fonseca", "Campos", "Siqueira", "Farias", "Pires", "Coelho", "Santana", "Bezerra",
    "Duarte", "Neves", "Leite", "Viana", "Cunha", "Araújo", "Borges", "Barros", "Antunes", "Braga",
    "Guimarães", "Tavares", "Batista", "Parente", "Bittencourt", "Macedo", "Azevedo", "Moraes", "Cardoso", "Camargo",
    "Peixoto", "Valente", "Rezende", "Castro", "Vieira", "Moura", "Magalhães", "Campos", "Barreto", "Ferraz",
    "Lacerda", "Galvão", "Brandão", "Rezende", "Frota", "Moraes", "Tavares", "Peixoto", "Siqueira", "Borges",
    "Carneiro", "Sampaio", "Couto", "Cavalcante", "Furtado", "Gomes", "Goulart", "Figueiredo", "Silveira", "Furtado",
    "Carmo", "Guedes", "Carvalho", "Oliveira", "Paiva", "Ramos", "Vasconcelos", "Muniz", "Queiroz", "Siqueira",
    "Marinho", "Almeida", "Campos", "Guedes", "Freire", "Henriques", "Porto", "Meireles", "Amaral", "Nóbrega",
    "Prado", "Ramos", "Saldanha", "Torres", "Pinto", "Xavier", "Cunha", "Oliveira", "Barros", "Lima",
    "Santana", "Pires", "Moraes", "Dantas", "Reis", "Figueira", "Mendes", "Cardoso", "Vaz", "Barbosa",
    "Macedo", "Freitas", "Monteiro", "Leite", "Duarte", "Cunha"
]

especialidades = [
    "clínica geral", "clínica geral", "clínica geral", "clínica geral", "clínica geral", "clínica geral", 
    "clínica geral", "clínica geral", "clínica geral", "clínica geral", "clínica geral", "clínica geral",
    "clínica geral", "clínica geral", "clínica geral", "clínica geral", "clínica geral", "clínica geral",
    "clínica geral", "clínica geral", 
    "ortopedia", "ortopedia", "ortopedia", "ortopedia", "ortopedia", "ortopedia", "ortopedia", 
    "ortopedia", "ortopedia", "ortopedia",  
    "dermatologia", "dermatologia", "dermatologia", "dermatologia", "dermatologia", "dermatologia",
    "dermatologia", "dermatologia", "dermatologia", "dermatologia",
    "pediatria", "pediatria", "pediatria", "pediatria", "pediatria", "pediatria", "pediatria", "pediatria",
    "pediatria", "pediatria",
    "cardiologia", "cardiologia", "cardiologia", "cardiologia", "cardiologia", "cardiologia", "cardiologia",
    "cardiologia", "cardiologia", "cardiologia" ]

all_nomes_rua = [
    "Rua das Flores", "Rua dos Girassóis", "Rua das Palmeiras", "Rua das Acácias", "Rua das Margaridas", "Rua dos Lírios",
    "Rua das Violetas", "Rua das Hortênsias", "Rua das Begônias", "Rua das Azaléias", "Rua das Orquídeas", "Rua dos Ipês",
    "Rua das Bromélias", "Rua das Camélias", "Rua das Dálias", "Rua das Rosas", "Rua dos Cravos", "Rua dos Jasmins",
    "Rua dos Amores", "Rua dos Abraços", "Rua dos Sonhos", "Rua da Paz", "Rua da Alegria", "Rua da Esperança", "Rua da Felicidade",
    "Rua da Harmonia", "Rua da Liberdade", "Rua da Serenidade", "Rua da Tranquilidade", "Rua da Amizade", "Rua da Solidariedade",
    "Rua da Fraternidade", "Rua da Compaixão", "Rua da Empatia", "Rua da Tolerância", "Rua da Paciência", "Rua da Generosidade",
    "Rua da Gratidão", "Rua da Bondade", "Rua da Simpatia", "Rua da Compreensão", "Rua da Sabedoria", "Rua da Verdade",
    "Rua da Justiça", "Rua da Honestidade", "Rua da Lealdade", "Rua da Integridade", "Rua da Responsabilidade", "Rua da Ética",
    "Rua da Moral", "Rua da Decência", "Rua da Consciência", "Rua da Empatia", "Rua da Empatia", "Rua da Sinceridade",
    "Rua da Sustentabilidade", "Rua da Ecologia", "Rua da Conservação", "Rua da Preservação", "Rua da Natureza", "Rua da Vida",
    "Rua do Bem", "Rua do Amor", "Rua do Carinho", "Rua da Afetividade", "Rua da Cumplicidade", "Rua da Harmonia",
    "Rua da Serenidade", "Rua da Paz Interior", "Rua da Felicidade", "Rua da Alegria de Viver", "Rua da Esperança", "Rua da Fé",
    "Rua do Encanto", "Rua da Magia", "Rua da Inspiração", "Rua do Encorajamento", "Rua da Motivação", "Rua da Determinação",
    "Rua da Coragem", "Rua da Força", "Rua da Resiliência", "Rua da Persistência", "Rua da Superação", "Rua da Vitória",
    "Rua da Conquista", "Rua da Realização", "Rua do Sucesso", "Rua da Prosperidade", "Rua da Abundância", "Rua da Fartura",
    "Rua da Fortuna", "Rua da Sorte", "Rua da Felicidade", "Rua do Contentamento", "Rua do Prazer", "Rua da Satisfação",
    "Rua da Harmonia", "Rua do Equilíbrio", "Rua da Paz", "Rua da Tranquilidade", "Rua da Serenidade", "Rua da Calma",
    "Rua da Quietude", "Rua da Meditação", "Rua da Contemplação", "Rua da Reflexão", "Rua da Sabedoria", "Rua da Consciência",
    "Rua do Conhecimento", "Rua da Inteligência", "Rua da Racionalidade", "Rua da Lucidez", "Rua da Perspicácia",
    "Rua da Clarividência", "Rua da Visão", "Rua da Imaginação", "Rua da Criatividade", "Rua da Inovação", "Rua da Inventividade",
    "Rua da Originalidade", "Rua da Singularidade", "Rua da Unicidade", "Rua da Individualidade", "Rua da Autenticidade",
    "Rua da Personalidade", "Rua da Identidade", "Rua da Essência", "Rua da Alma", "Rua do Espírito", "Rua do Coração",
    "Rua da Paixão", "Rua do Amor", "Rua da Afetividade", "Rua da Compaixão", "Rua da Empatia", "Rua da Solidariedade",
    "Rua da Fraternidade", "Rua da Irmandade", "Rua da União", "Rua da Amizade", "Rua da Cumplicidade", "Rua da Ternura",
    "Rua da Doçura", "Rua da Sensibilidade", "Rua da Vulnerabilidade", "Rua da Sinceridade", "Rua da Autenticidade",
    "Rua da Integridade", "Rua da Honestidade", "Rua da Lealdade", "Rua da Confiança", "Rua da Fidelidade", "Rua da Verdade",
    "Rua da Transparência", "Rua da Justiça", "Rua da Igualdade", "Rua da Equidade", "Rua da Equanimidade", "Rua da Imparcialidade",
    "Rua da Imunidade", "Rua da Isenção", "Rua da Liberdade", "Rua da Independência", "Rua da Autonomia", "Rua da Soberania",
    "Rua da Democracia", "Rua da Participação", "Rua da Representatividade", "Rua da Legitimidade", "Rua da Legalidade",
    "Rua da Constitucionalidade", "Rua da Institucionalidade", "Rua da Estabilidade", "Rua da Segurança", "Rua da Proteção",
    "Rua da Defesa", "Rua da Salvaguarda", "Rua da Preservação", "Rua da Conservação" ]

all_medicamentos = [
    "Paracetamol", "Ibuprofeno", "Dipirona", "Omeprazol", "Amoxicilina", "Diclofenaco",
    "Metformina", "Sinvastatina", "Cloridrato de Sertralina", "Losartana",
    "Clonazepam", "Levotiroxina", "Atorvastatina", "Hidroclorotiazida",
    "Captopril", "Citalopram", "Tramadol", "Rivotril", "Fluoxetina", "Diazepam", "Escitalopram",
    "Metronidazol", "Enalapril", "Pantoprazol", "Ciprofloxacino",
    "Salbutamol", "Tadalafil", "Salmeterol", "Dexmedetomidina", "Gabapentina", "Cloridrato de Lidocaína"
]
parametros_sintomas_chatgpt = ['Febre',
'Tosse', 'Dor de Cabeça', 'Náusea', 'Vômito', 'Dor Abdominal', 'Diarreia', 'Dor no Peito', 'Fadiga', 'Perda de Apetite',
'Dor Muscular', 'Dor nas Articulações', 'Calafrios', 'Suor Noturno', 'Congestão Nasal', 'Coriza', 'Espirros',
'Garganta Inflamada', 'Dificuldade para Respirar', 'Palpitações', 'Tontura', 'Vertigem', 'Dormência', 'Formigamento', 'Erupção Cutânea',
'Prurido (coceira)', 'Vermelhidão','Inchaço', 'Hemorragia', 'Visão Embaçada', 'Zumbido no Ouvido', 'Dor de Ouvido',
'Perda de Audição', 'Sensibilidade à Luz', 'Olhos Secos', 'Olhos Lacrimejantes', 'Dor Ocular', 'Manchas na Pele',
'Manchas nos Olhos', 'Lábios Rachados', 'Boca Seca', 'Úlceras na Boca', 'Halitose', 'Dificuldade para Engolir',
'Rouquidão', 'Dor na Lombar', 'Dor Cervical', 'Cãibras', 'Sensação de Queimação', 'Tremores', 'Cansaço', 'Distensão Abdominal',
'Gases', 'Constipação', 'Diarreia', 'Sangramento nas Gengivas', 'Mau Hálito', 'Tosse com Sangue', 'Falta de Ar',
'Taquicardia', 'Arritmia', 'Hipertensão', 'Hipotensão', 'Aumento de Peso', 'Perda de Peso', 'Insônia', 'Sonolência', 'Irritabilidade',
'Ansiedade', 'Depressão', 'Pensamentos Suicidas', 'Agitação', 'Confusão', 'Esquecimento', 'Alucinações', 'Delírios',
'Paranoia', 'Mania', 'Crises de Pânico', 'Tonturas', 'Desmaios', 'Problemas de Equilíbrio', 'Fraqueza Muscular',
'Tremores', 'Contraturas', 'Espasmos', 'Dormência nas Extremidades', 'Formigamento', 'Dor Crônica', 'Sensibilidade ao Tato',
'Fotofobia', 'Sensibilidade Sonora', 'Sensação de Cabeça Pesada', 'Tontura ao Levantar', 'Náusea Matinal',
'Azia', 'Indigestão', 'Refluxo Gastroesofágico', 'Barriga Inchada', 'Vontade Frequente de Urinar']

all_parametros_sintomas = [
    "Nome do sintoma", "Intensidade", "Duração", "Frequência", "Localização", "Início", "Fim",
    "Padrão", "Agravantes", "Aliviantes", "Acompanhantes", "Qualidade", "Periodicidade", "Evolução",
    "Horário de início", "Horário de término", "Constância", "Recorrência", "Triggers (Desencadeadores)",
    "Associação com alimentos", "Associação com medicamentos", "Associação com atividades", "Mudanças ao longo do dia",
    "Impacto na vida diária", "Sintomas associados", "Sintomas precedentes", "Sintomas subsequentes", "História familiar",
    "História médica", "História de alergias", "Efeito de tratamentos anteriores", "Medicações em uso", "Alterações no apetite",
    "Alterações no sono", "Alterações no humor", "Nível de energia", "Mobilidade", "Aparência física", "Mudanças na pele",
    "Zona afetada", "Tipo de dor", "Impacto emocional", "Impacto social", "Estilo de vida", "Exposição a fatores ambientais",
    "Exposição a fatores ocupacionais", "História de viagens", "Nível de estresse", "Fatores psicológicos",
    "Comportamentos de enfrentamento"
]

parametros_observacoes_metricas_chatgpt = [
('Temperatura Corporal (°C)', 37.2), ('Pressão Arterial Sistólica (mmHg)', 120), ('Pressão Arterial Diastólica (mmHg)', 80),
('Frequência Cardíaca (bpm)', 72), ('Frequência Respiratória (respirações/min)', 16), ('Saturação de Oxigênio (%)', 98),
('Índice de Massa Corporal (IMC)', 25.5), ('Glicemia em Jejum (mg/dL)', 90), ('Colesterol Total (mg/dL)', 180),
('HDL (mg/dL)', 50), ('LDL (mg/dL)', 120), ('Triglicerídeos (mg/dL)', 100), ('Hemoglobina (g/dL)', 14), ('Hematócrito (%)', 42),
('Contagem de Glóbulos Brancos (milhões/mL)', 7.5), ('Contagem de Plaquetas (milhões/mL)', 250), ('Taxa de Filtração Glomerular (mL/min)', 110),
('Creatinina Sérica (mg/dL)', 0.9), ('Bilirrubina Total (mg/dL)', 0.8), ('Volume Urinário (mL/24h)', 2000),
('Volume Sanguíneo (litros)', 5), ('Capacidade Pulmonar Total (litros)', 6), ('Volume Expiratório Forçado (litros)', 4),
('Capacidade Residual Funcional (litros)', 2), ('Débito Cardíaco (litros/min)', 5), ('Pressão Intracraniana (mmHg)', 10),
('Pressão Intraocular (mmHg)', 15), ('Pressão do Líquido Cefalorraquidiano (mmHg)', 18), ('Espessura da Camada de Gordura (mm)', 25), 
('Diâmetro Pupilar (mm)', 4), ('Taxa de Metabolismo Basal (kcal/dia)', 1600), ('Consumo de Oxigênio (mL/min/kg)', 250),
('Gasto Energético Total (kcal/dia)', 2000), ('Taxa de Excreção de Creatinina (mg/dL/h)', 15), ('Taxa de Excreção de Urina (mL/min)', 1.5),
('Concentração de Sódio no Sangue (mmol/L)', 140), ('Concentração de Potássio no Sangue (mmol/L)', 4), ('Concentração de Cálcio no Sangue (mg/dL)', 9),
('Concentração de Magnésio no Sangue (mg/dL)', 2), ('Concentração de Fósforo no Sangue (mg/dL)', 3), ('Concentração de Glicose no Líquido Cefalorraquidiano (mg/dL)', 60),
('Volume de Líquido Amniótico (mL)', 800), ('Espessura Endometrial (mm)', 10), ('Fluxo Sanguíneo Uterino (mL/min)', 120),
('Pressão Intrauterina (mmHg)', 12), ('Diâmetro da Cabeça Fetal (cm)', 34), ('Comprimento do Fêmur Fetal (cm)', 6),
('Peso Fetal Estimado (g)', 2500), ('Índice de Apgar (0-10)', 9), ('Tempo de Coagulação (segundos)', 8), ('Tempo de Protrombina (segundos)', 12),
('Tempo de Tromboplastina Parcial Ativada (segundos)', 25), ('Contagem de Células Tumorais Circulantes (células/mL)', 1000),
('Nível de Hemoglobina Glicada (%)', 5.5), ('Pressão Venosa Central (mmHg)', 8), ('Índice Tornozelo-Braquial', 1.0), ('Taxa de Efluxo Glomerular (mL/min)', 120),
('Fluxo Sanguíneo Coronariano (mL/min)', 70), ('Pressão Parcial de Oxigênio Arterial (mmHg)', 95), ('Pressão Parcial de Dióxido de Carbono Arterial (mmHg)', 40),
('Fração de Ejeção Cardíaca (%)', 60), ('Fração de Filtração Renal (%)', 20), ('Taxa de Filtração Glomerular Estimada (mL/min/1.73m²)', 100),
('Espessura da Intima-Média Carotídea (mm)', 0.8), ('Diâmetro Aórtico (cm)', 2.5), ('Resistência Vascular Sistêmica (mmHg/mL/min)', 20),
('Resistência Vascular Pulmonar (mmHg/mL/min)', 10), ('Espessura do Músculo Quadríceps (cm)', 3.5), ('Volume do Cisto Ovariano (mL)', 20),
('Diâmetro Maior do Tumor (cm)', 5), ('Diâmetro Menor do Tumor (cm)', 3), ('Nível de PSA (ng/mL)', 3.5), ('Nível de CA 125 (U/mL)', 20),
('Nível de CA 19-9 (U/mL)', 25), ('Volume Médio de Urina Produzida por Micção (mL)', 300), ('Volume de Sangue Circulante (litros)', 4.5),
('Volume do Hematoma (mL)', 10), ('Concentração de Oxigênio na Hemoglobina (%)', 98), ('Velocidade de Condução Nervosa (m/s)', 60),
('Tempo de Coagulação Ativado (segundos)', 30), ('Tempo de Lise do Coágulo (minutos)', 20)
]

all_parametros_observacoes_metricas = [
    "Temperatura corporal (°C)", "Pressão arterial (mmHg)", "Frequência cardíaca (bpm)", "Frequência respiratória (rpm)", 
    "Nível de dor (escala 0-10)", "Saturação de oxigênio (%)", "Peso (kg)", "Altura (cm)", "Índice de Massa Corporal (IMC)", 
    "Nível de glicose no sangue (mg/dL)", "Colesterol total (mg/dL)", "HDL (mg/dL)", "LDL (mg/dL)", "Triglicerídeos (mg/dL)", 
    "Hemoglobina (g/dL)", "Hematócrito (%)", "Leucócitos (10^3/μL)", "Plaquetas (10^3/μL)", "Creatinina (mg/dL)", "Ureia (mg/dL)"
]

localidades = [
    {"localidade": "Lisboa", "postal":"1000"},
    {"localidade": "Sintra", "postal": "2635"},
    {"localidade": "Cascais", "postal": "2750"},
    {"localidade": "Amadora", "postal": "1500"},
    {"localidade": "Oeiras", "postal": "2740"},
    {"localidade": "Loures", "postal": "1685"},
    {"localidade": "Almada", "postal": "2800"},
    {"localidade": "Barreiro", "postal": "2830"},
    {"localidade": "Seixal", "postal": "2840"},
    {"localidade": "Moita", "postal": "2860"},
    {"localidade": "Montijo", "postal": "2870"},
    {"localidade": "Odivelas", "postal": "1675"},
    {"localidade": "Vila Franca de Xira", "postal": "2600"},
    {"localidade": "Mafra", "postal": "2640"},
    {"localidade": "Torres Vedras", "postal": "2560"}
    ]

localidades_clinicas = [
    "Lisboa","Sintra", "Cascais", "Amadora", "Oeiras", "Loures", "Almada", 
    "Barreiro", "Seixal", "Moita", "Montijo", "Odivelas", "Vila Franca de Xira", 
    "Mafra", "Torres Vedras",
    ]

all_clinicas = [
    "clinica Medis", "clinica miMed", "clinica Core", "clinica Affidea", "clinica CUF"
]

all_NIF = set()  # Usando um conjunto para garantir a unicidade dos NIFs

all_telefones = set()  # Usando um conjunto para garantir a unicidade dos números de telefone

all_SSN = set()

all_codigo_SNS = set()

clinicas = []

medicamento_consulta = []

"""----------------------------------Abertura de Ficheiros-----------------------------------------"""

clinicas_file = open("./clinica.sql", "w")
medicos_file = open("./medico.sql", "w")
enfermeiros_file = open("./enfermeiro.sql", "w")
pacientes_file = open("./paciente.sql", "w")
trabalha_file = open("./trabalha.sql", "w")
consulta_file = open("./consulta.sql", "w")
receita_file = open("./receita.sql", "w")
observacao_file = open("./observacao.sql", "w")

populate_file = open("./populate.sql", "w")


"""---------------------------------Dicionariosss-------------------------------------------"""


enfermeiros_por_clinicas = {
    "clinica Medis":0,
    "clinica miMed":0,
    "clinica Core":0,
    "clinica Affidea":0,
    "clinica CUF":0,
}

medicos_por_clinicas = {
    "clinica Medis":0,
    "clinica miMed":0,
    "clinica Core":0,
    "clinica Affidea":0,
    "clinica CUF":0,
}

medico_dic ={
    "nif_medico": "", 
    "nome_medico": "",
    "telefone_medico": "",    
    "morada_medico": "",
    "especialidade": ""
}
medicos_lista = []

enfermeiro_dic ={
    "nif_enfermeiro": "", 
    "nome_enfermeiro": "",
    "telefone_enfermeiro": "",    
    "morada_enfermeiro": "",
    "nome_clinica_enfermeiro": ""
}
enfermeiros_lista = []

paciente_dic ={
    "nome_paciente": "",
    "telefone_paciente": "",
    "nif_paciente": "",
    "ssn_paciente": "",
    "morada_paciente": "",
    "data_nasc": "",
}
pacientes_lista = []

clinica_dic ={
    "nome_clinica": "",
    "telefone_clinica": "",
    "morada_clinica": "",
}
clinicas_lista = []

trabalha_dic ={
    "nome_clinica": "",
    "dia_da_semana_trabalho": "",
    "nif_medico": "",
}
trabalha_lista = []

consulta_dic ={
    "nome_clinica": "",
    "ssn_paciente": "",
    "nif_medico": "",
    "data_consulta": "",
    "hora_consulta": "",
    "codigo_sns": "",
}
consultas_lista = []

receita_dic ={
    "codigo_sns": "",
    "medicamento": "",
    "quantidade": "",
}
receitas_lista = []

medicos_clinicas = {
    "clinica Medis":[],
    "clinica miMed":[],
    "clinica Core":[],
    "clinica Affidea":[],
    "clinica CUF": [],
}



"""--------------------------------------------Counters------------------------------------------"""


counter_consultas = 0
counter_consultas_c_receitas = 0

"""----------------------------------------Funcoes piquenas cria-----------------------------------"""

#FUNCOES
def cria_nome(): #faz um nome random
    return random.choice(all_nomes) + " " + random.choice(all_apelidos)

def cria_nome_medico():
    
    nome = random.choice(all_nomes) + " " + random.choice(all_apelidos)
    for i in medicos_lista:
        if i.nome == nome:
            i = 0
            nome = random.choice(all_nomes) + " " + random.choice(all_apelidos)
    return nome

def cria_nif():  # Gera um NIF aleatório de 9 dígitos
    while True:
        nif = ''.join(random.choices('0123456789', k=9)) 
        if nif not in all_NIF:
            all_NIF.add(nif)  #trabalha com a lista para nao haver nifs repetidos
            return str(nif)

def cria_morada(): # morada do tipo : Rua A, 'codigo postal da localidade'-'nro random' Localidade
    numero_postal = ''.join(random.choices('1234567890', k=3))
    nro = random.randint(0, len(localidades) - 1)
    n_str = str(numero_postal)
    return random.choice(all_nomes_rua) + ", " + localidades[nro]["postal"] + "-" + n_str + " " + localidades[nro]["localidade"]

def cria_morada_clinica(): # morada do tipo : Rua A, 'codigo postal da localidade'-'nro random' Localidade
    local = random.choice(localidades_clinicas)
    for item in localidades:
        if item["localidade"] == local:
            localidades_clinicas.remove(local)
            local1 = item["localidade"]
            postal1 = item["postal"]
    
    numero_postal = ''.join(random.choices('1234567890', k=3))    
    return random.choice(all_nomes_rua) + ", " + postal1 + "-" + numero_postal + " " + local1


def cria_telefone():
    while True:
        telefone = '9' + ''.join(random.choices('0123456789', k=8))  # Gera um número de telefone aleatório começando com '9'
        if telefone not in all_telefones:
            all_telefones.add(telefone)  # Adiciona o número de telefone à lista
            return str(telefone)

def cria_clinica_nome():
    return random.choice(all_clinicas)


def cria_especialidade():
    if not especialidades:
        raise ValueError("Não há mais especialidades disponíveis")
    especialidade = random.choice(especialidades)
    especialidades.remove(especialidade)
    return especialidade

def cria_ssn():
    while True:
        ssn = ''.join(random.choices('0123456789', k=11)) 
        if ssn not in all_SSN:
            all_SSN.add(ssn)  #trabalha com a lista para nao haver SSNs repetidos
            return str(ssn)
        
def cria_codigo_sns():
    while True:
        codigo_SNS = ''.join(random.choices('0123456789', k=12)) 
        if codigo_SNS not in all_codigo_SNS:
            all_codigo_SNS.add(codigo_SNS)  #trabalha com a lista para nao haver codigo_SSNs repetidos
            return str(codigo_SNS)

def cria_data_nascimento():
    ano = random.randint(1924, 2023)
    mes = random.choice(range(1,12))
    dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dia = random.choice(range(1,dias_no_mes[mes - 1]))    
    return str(ano) + "-" + str(mes) + "-" + str(dia)

def cria_data_consulta():
    ano = random.randint(2023, 2025)
    mes = random.choice(range(1,12))
    if ano == 2023:
        dia = random.choise(range(1,dias_no_mes_23[mes - 1] ))
    else: #é 2024
        dia = random.choise(range(1,dias_no_mes_24[mes - 1] ))
    return str(ano) + "-" + str(mes) + "-" + str(dia)

def diz_dia_da_semana_escrito(data_string):
    data = datetime.datetime.strptime(data_string, '%Y-%m-%d').date()
    dia_semana_numero = data.weekday()
    dia_semana_escrito = calendar.day_name[dia_semana_numero]
    return dia_semana_escrito

def cria_hora_consulta():
    hora = random.choice([8, 9, 10, 11, 12, 14, 15, 16, 17, 18])
    minutos = random.choice(["00", "30"])
    return str(hora) + ":" + minutos

def cria_medicamentos_consulta():
    medicamentos_consulta = []
    nro_medicamentos = random.choice(range(1, 7))
    while len(medicamentos_consulta) < nro_medicamentos:
        medicamento = random.choice(all_medicamentos)
        if medicamento not in medicamentos_consulta:
            medicamentos_consulta.append(medicamento)            
    return medicamentos_consulta

def cria_quantidades(id_consulta):
    quantis = []
    nro = len(medicamento_consulta[id_consulta])
    for _ in range(nro):
        quant = random.choice(range(1, 4))
        quantis.append(quant)
    return quantis
        

def cria_clinica_enfermeiros(enfermeiros_por_clinicas):
    # Prioriza clínicas com menos de 5 enfermeiros
    clinicas_prioritarias = [clinica for clinica, count in enfermeiros_por_clinicas.items() if count < 5]
    if clinicas_prioritarias:
        return random.choice(clinicas_prioritarias)
    
    # Caso todas as clínicas tenham 5 ou mais enfermeiros, escolhe aleatoriamente uma com menos de 6
    clinicas_validas = [clinica for clinica, count in enfermeiros_por_clinicas.items() if count < 6]
    if clinicas_validas:
        return random.choice(clinicas_validas)
    
    # Se todas as clínicas tiverem 6 enfermeiros, retorna None
    return None          

def cria_observacoes_sintomas():
    sintomas_return = []
    n_sintomas = random.randint(1, 5)
    n = 0
    while(n < n_sintomas):
        sintoma_atual = random.choice(parametros_sintomas_chatgpt)
        if(sintoma_atual not in sintomas_return):
            sintomas_return.append(sintoma_atual)
            n+=1
    return sintomas_return

def cria_observacoes_metrica():
    metricas_return = []
    n_metricas = random.randint(0, 3)
    n = 0
    while(n < n_metricas):
        metrica_atual = random.choice(parametros_observacoes_metricas_chatgpt)
        if(metrica_atual not in metricas_return):
            metricas_return.append(metrica_atual)
            n+=1
    return metricas_return


"""---------------------------------Classes e Gera respetivo-----------------------------------------"""



class Clinica:
    #ha 5 clinicas em 3 localidades
    def __init__(self, nome) -> None:   
        self.nome = nome
        self.telefone = cria_telefone()
        self.morada = cria_morada_clinica()

def gera_clinicas():
    populate_file.write(f"INSERT INTO clinica (nome, telefone, morada) VALUES\n")
    for i in range(5):
        clinicas.append(Clinica(all_clinicas[i]))
        #print(clinicas[i].nome)
        populate_file.write(f"('{clinicas[i].nome}', '{clinicas[i].telefone}', '{clinicas[i].morada}'),\n")
    

class Enfermeiro:
    #max é 30 enfermeiros e minimo é 25
    def __init__(self) -> None:
        self.nif = cria_nif() #PK
        self.nome = cria_nome()
        self.telefone = cria_telefone()
        self.morada = cria_morada()

        clinica = cria_clinica_enfermeiros(enfermeiros_por_clinicas)
        while clinica is None:
            clinica = cria_clinica_enfermeiros(enfermeiros_por_clinicas)
        
        self.nome_clinica = clinica
        enfermeiros_por_clinicas[self.nome_clinica] += 1

def gera_enfermeiros():
    populate_file.write(f"INSERT INTO enfermeiro (nif, nome, telefone, morada, nome_clinica) VALUES\n")
    for i in range(random.choice(range(25, 30))):
        enfermeiros_lista.append(Enfermeiro())
        populate_file.write(f"('{enfermeiros_lista[i].nif}', '{enfermeiros_lista[i].nome}', '{enfermeiros_lista[i].telefone}', '{enfermeiros_lista[i].morada}', '{enfermeiros_lista[i].nome_clinica}'),\n")

class Medico:
    #ha 60 medicos
    def __init__(self) -> None:
        self.nif = cria_nif() #PK
        self.nome = cria_nome_medico()
        self.telefone = cria_telefone()
        self.morada = cria_morada()
        self.especialidade = cria_especialidade()

def gera_medico():
    populate_file.write(f"INSERT INTO medico (nif, nome, telefone, morada, especialidade) VALUES\n")
    for i in range(60):
        medicos_lista.append(Medico())
        populate_file.write(f"('{medicos_lista[i].nif}', '{medicos_lista[i].nome}', '{medicos_lista[i].telefone}', '{medicos_lista[i].morada}', '{medicos_lista[i].especialidade}'),\n")


class Paciente:
    #há cerca de 5000 pacientes
    def __init__(self, nif=None, nome=None, telefone=None, morada=None):
        if nif is not None:
            self.ssn = cria_ssn()
            self.nif = nif
            self.nome = nome
            self.telefone = telefone
            self.morada = morada
            self.data_nasc = cria_data_nascimento()
        else:
            self.ssn = cria_ssn()
            self.nif = cria_nif()
            self.nome = cria_nome()
            self.telefone = cria_telefone()
            self.morada = cria_morada()
            self.data_nasc = cria_data_nascimento()

def gera_paciente():
    populate_file.write(f"INSERT INTO paciente (ssn, nif, nome, telefone, morada, data_nasc) VALUES\n") 
    for i in range(5000):
        paciente = Paciente()
        pacientes_lista.append((paciente.ssn, paciente.nif))
        populate_file.write(f"('{paciente.ssn}', '{paciente.nif}', '{paciente.nome}', '{paciente.telefone}', '{paciente.morada}', '{paciente.data_nasc}'),\n")
    index = 5000
    for i in medicos_lista:
        paciente = Paciente(i.nif, i.nome, i.telefone, i.morada)
        pacientes_lista.append((paciente.ssn, paciente.nif))
        populate_file.write(f"('{paciente.ssn}', '{paciente.nif}', '{paciente.nome}', '{paciente.telefone}', '{paciente.morada}', '{paciente.data_nasc}'),\n")
        index+=1

def gera_trabalha():
    populate_file.write(f"INSERT INTO trabalha (nif, nome, dia_da_semana) VALUES\n")
    med_days = {}
    clinicas_done = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
    allEigths = False

    for i in medicos_lista:
        placeholder=[0,1,2,3,4]
        num_elements_to_pick = random.randint(2, 5)
        med_clinics = random.sample(placeholder, num_elements_to_pick)
        lastResort = []

        num_working_days = 7
        days_of_week = [0,1,2,3,4,5,6]
        for j in range(num_working_days):
            if not allEigths:
                if med_clinics:
                
                    clinic_choice = random.choice(med_clinics)
                    day = random.choice(days_of_week)
                    while clinicas_done[clinic_choice][day] == 8:
                        clinic_choice = random.choice(med_clinics)
                        day = random.choice(days_of_week)

                    lastResort.append(clinic_choice)
                    med_clinics.remove(clinic_choice)
                    days_of_week.remove(day)

                    med_days[(i.nif, day)] = clinicas[clinic_choice].nome
                else:
                    clinic_choice = random.choice(lastResort)
                    day = random.choice(days_of_week)

                    while(clinicas_done[clinic_choice][day] == 8):
                        clinic_choice = random.choice(lastResort)
                        day = random.choice(days_of_week)

                    days_of_week.remove(day)
                    
                    med_days[(i.nif, day)] = clinicas[clinic_choice].nome

                
                allEigths = ((clinicas_done[0].count(8) == len(clinicas_done[0]) if clinicas_done[0] else True) and (clinicas_done[1].count(8) == len(clinicas_done[1]) if clinicas_done[1] else True)and (clinicas_done[2].count(8) == len(clinicas_done[2]) if clinicas_done[2] else True)and (clinicas_done[3].count(8) == len(clinicas_done[3]) if clinicas_done[3] else True)and (clinicas_done[4].count(8) == len(clinicas_done[4]) if clinicas_done[4] else True))
            
            else:
                if med_clinics:
                    
                    clinic_choice = random.choice(med_clinics)
                    day = random.choice(days_of_week)

                    lastResort.append(clinic_choice)
                    med_clinics.remove(clinic_choice)
                    days_of_week.remove(day)
                    
                    med_days[(i.nif, day)] = clinicas[clinic_choice].nome
                    
                else:
                    clinic_choice = random.choice(lastResort)
                    day = random.choice(days_of_week)
    
                    days_of_week.remove(day)
                    
                    med_days[(i.nif, day)] = clinicas[clinic_choice].nome


    for key in med_days:
        populate_file.write(f"('{key[0]}', '{med_days[key]}', {key[1]}),\n")
        trabalha_lista.append((key[0], med_days[key], key[1]))





def gera_consultas():
    data_comparacao = datetime(2024, 5, 31)
    populate_file.write(f"INSERT INTO consulta (ssn, nif, nome, data, hora, codigo_sns) VALUES\n")
    id = 0
    pacientes_sem_c = copy.deepcopy(pacientes_lista)
    return_value = 0
    for year in [2023, 2024]:
        if year == 2023:
            days = dias_no_mes_23
        else:
            days = dias_no_mes_24
        for month in range(1, 13):
            for day in range(1, days[month-1] + 1):
                date = datetime(year, month, day)
                if (date == data_comparacao):
                    return_value = id
                weekday = date.weekday()

                pacientes_consulta = []
                for clinica in clinicas:
                    medicos_consulta = []
                    medicos_lista_clinica_dia = [medico.nif for medico in medicos_lista if (medico.nif, clinica.nome, weekday) in trabalha_lista]
                    daily_consultas = 0
                    medicos_falta = True
                    while(daily_consultas < 20):
                        if (medicos_falta):
                            for medico in medicos_lista_clinica_dia:
                                for i in range(2):
                                    if (pacientes_sem_c):
                                        paciente = random.choice(pacientes_sem_c)
                                        while (paciente[1] == medico):
                                            paciente = random.choice(pacientes_sem_c)
                                        
                                        horas_consulta = cria_hora_consulta()

                                        while ((paciente[0], horas_consulta) in pacientes_consulta or \
                                            (medico, horas_consulta) in medicos_consulta):
                                            horas_consulta = cria_hora_consulta()
                            
                                        if (date > data_comparacao):
                                            populate_file.write(f"('{paciente[0]}', '{medico}', '{clinica.nome}', '{str(year) + '-' + str(month) + '-' + str(day)}', '{horas_consulta}', NULL),\n")
                                        else:
                                            codigo_sns = cria_codigo_sns()
                                            populate_file.write(f"('{paciente[0]}', '{medico}', '{clinica.nome}', '{str(year) + '-' + str(month) + '-' + str(day)}', '{horas_consulta}', '{codigo_sns}'),\n")
                                            consultas_lista.append(codigo_sns)
                                        id+= 1
                                        medicos_consulta.append((medico, horas_consulta))
                                        pacientes_consulta.append((paciente[0], horas_consulta))
                                        daily_consultas += 1
                                        pacientes_sem_c.remove(paciente)

                                    else:
                                        paciente = random.choice(pacientes_lista)
                                        while (paciente[1] == medico):
                                            paciente = random.choice(pacientes_lista)
                                        
                                        horas_consulta = cria_hora_consulta()

                                        while ((paciente[0], horas_consulta) in pacientes_consulta or \
                                            (medico, horas_consulta) in medicos_consulta):
                                            horas_consulta = cria_hora_consulta()
                                        
                                        if (date > data_comparacao):
                                            populate_file.write(f"('{paciente[0]}', '{medico}', '{clinica.nome}', '{str(year) + '-' + str(month) + '-' + str(day)}', '{horas_consulta}', NULL),\n")
                                        else:
                                            codigo_sns = cria_codigo_sns()
                                            populate_file.write(f"('{paciente[0]}', '{medico}', '{clinica.nome}', '{str(year) + '-' + str(month) + '-' + str(day)}', '{horas_consulta}', '{codigo_sns}'),\n")
                                            consultas_lista.append(codigo_sns)
                                        id+= 1
                                        medicos_consulta.append((medico, horas_consulta))
                                        pacientes_consulta.append((paciente[0], horas_consulta))
                                        daily_consultas += 1

                                
                            medicos_falta = False
                        else:
                            if (pacientes_sem_c):
                                paciente = random.choice(pacientes_sem_c)
                                medico = random.choice(medicos_lista_clinica_dia)

                                while (paciente[1] == medico):
                                    paciente = random.choice(pacientes_sem_c)
                                    medico = random.choice(medicos_lista_clinica_dia)
                                
                                horas_consulta = cria_hora_consulta()

                                while ((paciente[0], horas_consulta) in pacientes_consulta or \
                                    (medico, horas_consulta) in medicos_consulta):
                                    horas_consulta = cria_hora_consulta()
                                
                                if (date > data_comparacao):
                                    populate_file.write(f"('{paciente[0]}', '{medico}', '{clinica.nome}', '{str(year) + '-' + str(month) + '-' + str(day)}', '{horas_consulta}', NULL),\n")
                                else:
                                    codigo_sns = cria_codigo_sns()
                                    populate_file.write(f"('{paciente[0]}', '{medico}', '{clinica.nome}', '{str(year) + '-' + str(month) + '-' + str(day)}', '{horas_consulta}', '{codigo_sns}'),\n")
                                    consultas_lista.append(codigo_sns)

                                id+= 1
                                medicos_consulta.append((medico, horas_consulta))
                                pacientes_consulta.append((paciente[0], horas_consulta))
                                daily_consultas += 1
                                pacientes_sem_c.remove(paciente)

                            else:
                                paciente = random.choice(pacientes_lista)
                                medico = random.choice(medicos_lista_clinica_dia)

                                while (paciente[1] == medico):
                                    paciente = random.choice(pacientes_lista)
                                    medico = random.choice(medicos_lista_clinica_dia)
                                
                                horas_consulta = cria_hora_consulta()

                                while ((paciente[0], horas_consulta) in pacientes_consulta or \
                                    (medico, horas_consulta) in medicos_consulta):
                                    horas_consulta = cria_hora_consulta()
                                
                                if (date > data_comparacao):
                                    populate_file.write(f"('{paciente[0]}', '{medico}', '{clinica.nome}', '{str(year) + '-' + str(month) + '-' + str(day)}', '{horas_consulta}', NULL),\n")
                                else:
                                    codigo_sns = cria_codigo_sns()
                                    populate_file.write(f"('{paciente[0]}', '{medico}', '{clinica.nome}', '{str(year) + '-' + str(month) + '-' + str(day)}', '{horas_consulta}', '{codigo_sns}'),\n")
                                    consultas_lista.append(codigo_sns)

                                id+= 1
                                medicos_consulta.append((medico, horas_consulta))
                                pacientes_consulta.append((paciente[0], horas_consulta))
                                daily_consultas += 1
    return return_value

def gera_receita(id_counter_consulta):
    populate_file.write(f"INSERT INTO receita (codigo_sns, medicamento, quantidade) VALUES\n")
    a = id_counter_consulta * 0.8
    consultas_c_receitas = int(a)
    i = 0
    for i in range(consultas_c_receitas):
        codigo_sns = consultas_lista[i]
        medicamentos_lista = cria_medicamentos_consulta()
        for medicamento in medicamentos_lista:
            quantidade = random.randint(1,3)
            populate_file.write(f"('{codigo_sns}', '{medicamento}', {quantidade}),\n")    

def gera_observacao(id_counter_consultas):
    populate_file.write(f"INSERT INTO observacao (id, parametro, valor) VALUES\n")
    for i in range(1, id_counter_consultas + 1):
        observacoes_sintomas = cria_observacoes_sintomas()
        observacoes_metricas = cria_observacoes_metrica()
        for observacao_sint in observacoes_sintomas:
            populate_file.write(f"({i}, '{observacao_sint}', NULL),\n")
        for observacao_metric in observacoes_metricas:
            populate_file.write(f"({i}, '{observacao_metric[0]}', {random.uniform(10,50)}),\n")

gera_clinicas()
gera_medico()
gera_enfermeiros()
gera_paciente()
gera_trabalha()
id_counter_consultas = gera_consultas()
gera_receita(id_counter_consultas)
gera_observacao(id_counter_consultas)