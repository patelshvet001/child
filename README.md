# 🏥 Child Vaccination Management System

A Django-based web application for managing child vaccination records and appointments.

## 📋 Project Overview

This system allows hospitals to manage child vaccination records and parents to track their children's vaccination schedules. It includes features for appointment scheduling, vaccination record management, and digital certificate generation.

## ✨ Features

- 👥 User Authentication (Hospital and Patient accounts)
- 📅 Appointment Scheduling
- 📝 Vaccination Record Management
- 📜 Digital Certificate Generation with QR Code
- 👤 Profile Management
- ❓ FAQ Section
- 🔑 Password Reset Functionality
- 🔍 Advanced Search and Filtering
- 📊 Data Export (Excel and PDF)
- 📈 Real-time Statistics Dashboard

## ⚙️ Prerequisites

- 🐍 Python 3.x
- 🎯 Django
- 🗄️ MySQL Server
- 📦 Required Python packages:
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
  xlsxwriter>=3.0.0
  reportlab>=4.0.0
  ```

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd child
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\Activate.ps1
   # On Unix or MacOS
   source venv/bin/activate
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
   pip install xlsxwriter
   pip install reportlab
   ```

5. Install static files:
   ```bash
   python manage.py collectstatic
   ```

## 📁 Project Structure

- `happ/` - Main application for user authentication and core functionality
- `childvc/` - Application handling vaccination records and certificates
- `hospital/` - Application for hospital-specific functionality
- `manage.py` - Django's command-line utility for administrative tasks

## ⚡ Setup

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

## 💻 Usage

1. Access the admin panel at `/admin/`
2. Register as a hospital or patient
3. Schedule appointments and manage vaccination records
4. Generate digital certificates with QR codes
5. Use the search functionality to filter and export data:
   - 🔍 Search by patient name
   - 💉 Filter by vaccine type
   - 📊 Filter by appointment status
   - 📅 Filter by date range
   - 📥 Export data to Excel or PDF
   - 📈 View real-time statistics

## 📊 Export Functionality

The system provides two types of data export:

1. 📈 Excel Export:
   - Click the "Export to Excel" button
   - Downloads an Excel file with all vaccination data
   - Includes proper formatting and column headers
   - Maintains all search filters

2. 📄 PDF Export:
   - Click the "Export to PDF" button
   - Downloads a PDF file with formatted vaccination data
   - Includes title, date, and properly formatted table
   - Maintains all search filters

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details. 