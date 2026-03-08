# Kabiero School Management System

A comprehensive School ERP system built with Django for managing students, finance, attendance, and academic results.

## Features

### 🎓 Student Management
- Student registration and profiles
- Admission number tracking
- Grade management
- Parent contact information

### 💰 Finance Management
- Fee structure by grade
- Payment recording (Cash, MPESA, Bank)
- Automatic balance calculation
- Student fee dashboard
- Bursar dashboard with analytics
- MPESA payment integration

### 📊 Academic Results
- Teacher marks entry
- Automatic grade calculation
- Student results dashboard
- SMS notifications to parents
- Report card generation

### 📅 Attendance System
- Daily attendance tracking
- Attendance history
- Reports and analytics

### 📱 Parent Communication
- SMS notifications for results
- Payment confirmations
- Real-time updates

### 🎨 Modern UI
- Professional Jazzmin admin interface
- Responsive design
- Modern gradient styling
- Analytics dashboard

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Kabiero.git
cd Kabiero
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run server:
```bash
python manage.py runserver
```

## Tech Stack

- Django 4.2.7
- SQLite Database
- Django Jazzmin (Admin UI)
- Bootstrap/Custom CSS

## Project Structure

```
Kabiero/
├── accounts/       # Student & Staff management
├── finance/        # Fee & Payment management
├── academics/      # Results & Grades
├── attendance/     # Attendance tracking
├── core/           # Main website pages
├── templates/      # HTML templates
├── static/         # CSS, JS, Images
└── backend/        # Django settings
```

## License

MIT License

## Author

Kabiero Academy
