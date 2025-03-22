# Django Project

## Overview
This is a Django-based web application that provides boilerplate for JWTAuthentication

## Features
- User Registration
- User Authentication using JWT
- Token Refresh
- Authentication using JWT
- PostgreSQL database support
- RESTful API with Django REST Framework (DRF)

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (Simple JWT)
- **Containerization:** Docker, Docker Compose 

## Installation

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- PostgreSQL
- Virtualenv
- Docker & Docker Compose (optional)

### Steps
1. **Clone the repository**
   ```bash
   git clone git@github.com:asm-2000/django_boilerplate.git
   cd django_boilerplate
   ```
2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up the database**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser** (for accessing the admin panel)
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server**
   ```bash
   python manage.py runserver
   ```
7. **Access the application**
   - API Documentation: `http://127.0.0.1:8000/backend/api/swagger/`
   - Admin Panel: `http://127.0.0.1:8000/backend/api/admin/`

## Environment Variables
Create a `.env` file and configure the variables included in the .env.sample

## Running with Docker
1. **Build and start the containers**
   ```bash
   docker-compose up --build
   ```
2. **Access the application**
   - API Documentation: `http://localhost:8000/backend/api/swagger/`
   - Admin Panel: `http://localhost:8000/backend/api/admin/`

