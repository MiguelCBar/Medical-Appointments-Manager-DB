# Medical Appointments Manager (Databases Project)

## Description
This project is a **Medical Appointments Manager** implemented using Python and Flask. It serves as an interface to manage medical appointments, clinics, and their associated data stored in a PostgreSQL database. The system validates input, handles queries, and provides endpoints for listing clinics, specialties, doctors, and their available schedules. Additionally, it enables creating and canceling appointments with strict validation rules.

The report documentation is in Portuguese.

## Features
1. Clinic and Specialty Management:
    - List all clinics with their names and addresses.
    - Retrieve specialties offered at a specific clinic.

2. Doctor and Appointment Queries:
    - List doctors of a specific specialty working at a clinic along with their first three available time slots.
    - Register a medical appointment for a patient.
    - Cancel an upcoming appointment for a patient.

3. Data Validation:
    - Validate SSN (Social Security Number) and NIF (Tax Identification Number) for correct formats.
    - Validate appointment date and time for availability, working hours, and scheduling rules.

4. Database Connection:
    - Efficiently interacts with the database using a connection pool for optimized performance.
    - Protects against invalid or duplicate entries.

5. Logging:
    - Configured logging for monitoring application activity, debugging, and error tracking.

## Requirements
- Python 3.8+
- PostgreSQL
- Flask

## Credits
This project was developed by [Miguel Barbosa](https://github.com/MiguelCBar/), [David Quintino](https://github.com/QuintinoDavid/) and [Matilde Santos](https://github.com/matilde2004/).