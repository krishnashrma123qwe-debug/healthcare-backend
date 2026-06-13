# Healthcare Backend

A simple Django backend for managing patients, doctors, and their assignments.

## Setup

1. Clone this repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and set up your database config. (Uses SQLite by default).
5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Start the server:
   ```bash
   python manage.py runserver
   ```

## Endpoints

### Auth
- `POST /api/auth/register/` - Create a new user account
- `POST /api/auth/login/` - Login and get JWT

### Patients
- `POST /api/patients/` - Add a patient
- `GET /api/patients/` - List your patients
- `GET /api/patients/<id>/` - Get patient details
- `PUT /api/patients/<id>/` - Update patient
- `DELETE /api/patients/<id>/` - Delete patient

### Doctors
- `POST /api/doctors/` - Add a doctor
- `GET /api/doctors/` - List all doctors
- `GET /api/doctors/<id>/` - Get doctor details
- `PUT /api/doctors/<id>/` - Update doctor
- `DELETE /api/doctors/<id>/` - Delete doctor

### Mappings
- `POST /api/mappings/` - Assign doctor to patient
- `GET /api/mappings/` - List all assignments
- `GET /api/mappings/<patient_id>/` - Get doctors for a patient
- `DELETE /api/mappings/<id>/delete/` - Remove assignment

## Built With
- Django
- Django REST Framework
- djangorestframework-simplejwt
