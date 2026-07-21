# Task Manager REST API

A Django REST Framework application that provides JWT authentication and role-based task management.

# Tech Stack

Python
Django
Django REST Framework
SimpleJWT
SQLite

# Installation Steps
git clone <repository_url>
cd task_manager

python -m venv venv

virtual_env\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

<!-- Authentication -->

Register: POST /api/auth/register/
Login: POST /api/auth/login/
Refresh: POST /api/auth/refresh/
Profile: GET /api/auth/profile/

<!-- Task APIs -->

GET /api/tasks/
POST /api/tasks/
GET /api/tasks/<id>/
PUT /api/tasks/<id>/
PATCH /api/tasks/<id>/
DELETE /api/tasks/<id>/
<!-- RBAC -->
# 1-- Admin
        View, edit, and delete all tasks
# 2-- User
        View and manage only their own tasks

# final project structure

task_manager/
│
├── accounts/
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── signals.py
│   └── apps.py
│
├── tasks/
│   ├── admin.py
│   ├── filters.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
<!-- ├── config/ -->
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── Dockerfile
└── docker-compose.yml