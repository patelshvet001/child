# Child Vaccination Management System

A Django-based web application for managing child vaccination records and appointments.

## Project Overview

This system allows hospitals to manage child vaccination records and parents to track their children's vaccination schedules. It includes features for appointment scheduling, vaccination record management, and digital certificate generation.

## Features

- User Authentication (Hospital and Patient accounts)
- Appointment Scheduling
- Vaccination Record Management
- Digital Certificate Generation with QR Code
- Profile Management
- FAQ Section
- Password Reset Functionality

## Prerequisites

- Python 3.x
- Django
- Other required Python packages

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd child
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Install additional required packages:
   ```bash
   pip install django
   pip install Pillow
   pip install reportlab
   pip install qrcode
   pip install python-dateutil
   pip install django-crispy-forms
   pip install crispy-bootstrap4
   pip install django-allauth
   pip install django-environ
   ```

5. Install static files:
   ```bash
   python manage.py collectstatic
   ```

## Required Python Packages

```
Django>=3.2.0
Pillow>=8.0.0
reportlab>=3.6.0
qrcode>=7.0.0
python-dateutil>=2.8.2
django-crispy-forms>=1.14.0
crispy-bootstrap4>=1.0.0
django-allauth>=0.45.0
django-environ>=0.8.1
```

## Project Structure

- `happ/` - Main application for user authentication and core functionality
- `childvc/` - Application handling vaccination records and certificates
- `hospital/` - Application for hospital-specific functionality
- `manage.py` - Django's command-line utility for administrative tasks

## Setup

1. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the admin panel at `/admin/`
2. Register as a hospital or patient
3. Schedule appointments and manage vaccination records
4. Generate digital certificates with QR codes

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 