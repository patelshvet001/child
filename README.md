# 🏥 Child Vaccination Management System

<div align="center">

A comprehensive Django-based web application for managing child vaccination records and appointments.

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-3.2.0-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-red.svg)](LICENSE)

</div>

---

## 📋 Project Overview

This system facilitates efficient management of child vaccination records and appointments, providing a seamless experience for both healthcare providers and parents. It offers comprehensive features for appointment scheduling, vaccination record management, and digital certificate generation.

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 👥 User Authentication | Separate accounts for hospitals and patients |
| 📅 Appointment Management | Easy scheduling and tracking of appointments |
| 📝 Record Management | Comprehensive vaccination record keeping |
| 📜 Digital Certificates | QR code-enabled digital vaccination certificates |
| 👤 Profile System | User profile management and customization |
| ❓ FAQ Section | Comprehensive help and support system |
| 🔑 Security | Secure password reset and authentication |
| 🔍 Advanced Search | Sophisticated filtering and search capabilities |
| 📊 Data Export | Excel and PDF export functionality |
| 📈 Analytics | Real-time statistics and reporting |

## ⚙️ Technical Requirements

### System Prerequisites
- 🐍 Python 3.x
- 🎯 Django Framework
- 🗄️ MySQL Server

### 📦 Dependencies
```txt
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

## 🚀 Getting Started

### 1. Repository Setup
```bash
git clone <repository-url>
cd child
```

### 2. Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
.\venv\Scripts\Activate.ps1
# Unix/MacOS
source venv/bin/activate
```

### 3. Dependencies Installation

#### Important: Install these packages first
```bash
# Core Django and essential packages
pip install django
pip install Pillow
pip install reportlab
pip install qrcode
pip install python-dateutil

# Django extensions and forms
pip install django-crispy-forms
pip install crispy-bootstrap4
pip install django-allauth
pip install django-environ

# Export functionality packages
pip install xlsxwriter
pip install reportlab
```

#### Alternative: Install from requirements.txt
```bash
pip install -r requirements.txt
```

### 4. Static Files
```bash
python manage.py collectstatic
```

## 📁 Project Architecture

```
child/
├── happ/           # Core authentication and functionality
├── childvc/        # Vaccination records and certificates
├── hospital/       # Hospital-specific features
└── manage.py       # Django management utility
```

## ⚡ System Configuration

### 1. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Admin Account Creation
```bash
python manage.py createsuperuser
```

### 3. Development Server
```bash
python manage.py runserver
```

## 💻 User Guide

### Core Functionality
1. Access the admin panel at `/admin/`
2. Register as a hospital or patient
3. Schedule and manage appointments
4. Generate digital certificates

### Advanced Features
- 🔍 Patient name search
- 💉 Vaccine type filtering
- 📊 Appointment status tracking
- 📅 Date range selection
- 📥 Data export capabilities
- 📈 Statistical analysis

## 📊 Data Export Features

### Excel Export
- One-click export functionality
- Structured data presentation
- Customizable column headers
- Filtered data export

### PDF Export
- Professional document formatting
- Automated date stamping
- Tabular data presentation
- Search filter preservation

## 🤝 Contributing Guidelines

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Submit a Pull Request

## 📄 License Information

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for detailed information.

---

<div align="center">
Made with ❤️ for better healthcare management
</div> 