<<<<<<< HEAD
=======
<<<<<<< HEAD
# 📋 Task Manager REST API

A **Task Manager REST API** built using **Django REST Framework (DRF)** that provides secure **JWT-based authentication** and **Role-Based Access Control (RBAC)** for managing tasks.

This project was developed as part of a **Django Intern Assessment** to demonstrate backend development skills, REST API design, authentication, authorization, and CRUD operations using Django REST Framework.

---

# 🚀 Features

- User Registration
- JWT Authentication (Access & Refresh Tokens)
- User Profile API
- Task CRUD Operations
- Role-Based Access Control (RBAC)
- Search Tasks
- Filter Tasks
- Ordering
- Django Admin Panel
- API Testing using Postman

---

# 🛠 Tech Stack

| Technology | Version |
|------------|----------|
| Python | 3.9+ |
| Django | 4.x+ |
| Django REST Framework | Latest |
| SimpleJWT | Latest |
| SQLite | Default Database |
| Postman | API Testing |

---

# 📁 Project Structure

```
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
├── config/
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
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone "https://github.com/Shashank5h3/task_manage.git"
cd task_manager
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv virtual_env
```

Activate the virtual environment

```bash
virtual_env\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Create Superuser

```bash
python manage.py createsuperuser
```

---

## 6. Run the Development Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

# 🔐 Authentication

The project uses **JSON Web Token (JWT)** authentication provided by **djangorestframework-simplejwt**.

After successful login, two tokens are generated:

- Access Token
- Refresh Token

The Access Token is used to access protected APIs.

Example Header

```
Authorization: Bearer <access_token>
```

When the Access Token expires, use the Refresh Token to generate a new Access Token.

---

# 👥 Role-Based Access Control (RBAC)

The application supports two roles.

## Admin

An Admin can

- View all tasks
- Create tasks
- Update any task
- Delete any task
- Search all tasks
- Filter all tasks

---

## User

A User can

- View only their own tasks
- Create their own tasks
- Update only their own tasks
- Delete only their own tasks

---

# 📌 API Endpoints

## Authentication APIs

| Method | Endpoint | Description |
|----------|---------------------------|-----------------------------|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Login and receive JWT tokens |
| POST | `/api/auth/refresh/` | Generate a new Access Token |
| GET | `/api/auth/profile/` | Get logged-in user's profile |

---

## Task APIs

| Method | Endpoint | Description |
|----------|---------------------------|------------------------------|
| GET | `/api/tasks/` | List tasks |
| POST | `/api/tasks/` | Create a task |
| GET | `/api/tasks/<id>/` | Retrieve a task |
| PUT | `/api/tasks/<id>/` | Update a task |
| PATCH | `/api/tasks/<id>/` | Partially update a task |
| DELETE | `/api/tasks/<id>/` | Delete a task |

---

# 🔍 Search

Search tasks using title or description.

Example

```
GET /api/tasks/?search=django
```

---

# 🎯 Filtering

Filter tasks using status or owner.

Examples

```
GET /api/tasks/?status=true

GET /api/tasks/?owner=1
```

# ↕️ Ordering

Tasks can be ordered by

- created_at
- updated_at
- due_date

Example

```
GET /api/tasks/?ordering=due_date
```

# 📮 API Testing

All REST APIs were tested using **Postman**.

The following endpoints were verified:

- User Registration
- User Login
- User Profile
- Create Task
- Retrieve Tasks
- Update Task
- Partial Update Task
- Delete Task
- RBAC Authorization
- Search
- Filtering



=======
>>>>>>> 69b5b43 (Updated Task Manager API with RBAC, JWT, README and improvements)
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
<<<<<<< HEAD
└── docker-compose.yml
=======
└── docker-compose.yml

