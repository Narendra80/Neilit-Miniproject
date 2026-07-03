# 🚀 Django Full-Stack Masterclass — Live Classroom Demo & Capstone Repository
**Trainer:** GuruCharan Tanneeru  
**Topics Covered:** Django Fundamentals, MVT Architecture, ORM & Database Integration, CRUD Operations, Security, Session Management, and Frontend Integration with Bootstrap 5.

> 📘 **Looking for topic-by-topic slide explanations and trainer speaking notes?**  
> Check out the complete companion guide: **[`PRESENTATION_TOPICS_EXPLAINED.md`](file:///d:/Django/PRESENTATION_TOPICS_EXPLAINED.md)**!
> 
> 📝 **Want a line-by-line breakdown of every file and WHY we wrote each code block?**  
> Check out the code walkthrough guide: **[`createfile.md`](file:///d:/Django/createfile.md)**!

---

## 📌 1. Project Overview & Objectives
This repository is a complete, production-ready teaching and demonstration suite designed for live classroom sessions. It includes two core applications:
1. **`employee` (Module 3 Capstone App)**: A full-featured Employee Management Portal demonstrating MVT architecture, Function-Based Views (FBV), Class-Based Views (CBV), form validation, CSRF security, session storage, and complete ORM CRUD operations.
2. **`student` (Module 2 Demo App)**: A student roster demonstration focusing on modern UI design, template inheritance, and data presentation.

---

## 📂 2. Project Architecture & Directory Structure
Django follows the **MVT (Model-View-Template)** architectural pattern:
* **Model (`models.py`)**: Defines the data structure and talks to the database (ORM).
* **View (`views.py`)**: Contains application business logic and handles HTTP request/response flow.
* **Template (`templates/`)**: Renders HTML presentation and injects dynamic context variables.

```text
d:\Django\
│
├── README.md                          # Master project & classroom documentation (This File)
├── Module 3.pptx                      # Module 3 Presentation Slides
├── venv\                              # Python virtual environment
│
└── myproject\                         # Main Django project container
    ├── manage.py                      # Django command-line utility
    ├── db.sqlite3                     # Database file (SQLite by default, MySQL ready)
    │
    ├── myproject\                     # Global Project Configuration
    │   ├── __init__.py
    │   ├── settings.py                # Database, installed apps & static configuration
    │   ├── urls.py                    # Root URL router linking app routes
    │   └── wsgi.py / asgi.py          # Production server gateway interfaces
    │
    ├── employee\                      # ⭐ Module 3 App: Employee Management System
    │   ├── models.py                  # Employee database table definition
    │   ├── views.py                   # FBV, CBV, CRUD, Search, and Session views
    │   ├── urls.py                    # App-level routing (/employee/...)
    │   ├── admin.py                   # Django Admin portal registration
    │   ├── static\css\style.css       # Custom static styling
    │   └── templates\employee\        # HTML templates (base, home, list, form, session)
    │
    └── student\                       # ⭐ Module 2 App: Student Roster Demo
        ├── models.py, views.py, etc.
```

---

## 🛠️ 3. Step-by-Step Implementation Guide (From Start to End)

Here is the exact step-by-step workflow we followed to build this complete application:

### Step 1: Environment Setup, Project & App Initialization
We started by creating an isolated Python virtual environment, installing Django, initializing the root project, and creating our specialized `employee` application using Django's built-in CLI:
```bash
# 1. Create a Python virtual environment
python -m venv venv

# 2. Activate the virtual environment
# On Windows (PowerShell / CMD):
venv\Scripts\activate
# On macOS / Linux:
# source venv/bin/activate

# 3. Install Django framework and required drivers
pip install django
pip install django mysqlclient

# 4. Create the root Django project
django-admin startproject myproject

# 5. Enter the project directory
cd myproject

# 6. Create the employee application module
python manage.py startapp employee
```

### Step 2: App Registration & Settings Configuration
In `myproject/settings.py`, we registered `'employee'` inside `INSTALLED_APPS` so Django recognizes its models, templates, and migrations:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'student',
    'employee',  # <-- Added Module 3 Application
]
```

### Step 3: Database Models & Django ORM (`models.py`)
In `employee/models.py`, we created the Python class mapping directly to the relational database table without raw SQL:
```python
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    department = models.CharField(max_length=50, default="General")
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=50000.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

We then generated and executed database migrations:
```bash
python manage.py makemigrations employee
python manage.py migrate
```

### Step 4: Django Admin Panel Registration (`admin.py`)
In `employee/admin.py`, we registered the model with a custom `ModelAdmin` to instantly generate an enterprise-grade GUI for administrative management:
```python
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department', 'salary', 'created_at')
    search_fields = ('name', 'email', 'department')
    list_filter = ('department', 'created_at')
```

### Step 5: URL Routing & Views Implementation (`views.py` & `urls.py`)
We built a rich controller layer in `employee/views.py` demonstrating all core view concepts:
* **Function-Based Views (FBV)**: `home(request)` rendering templates with variables.
* **Class-Based Views (CBV)**: `HomeView(View)` demonstrating OOP reusability.
* **CRUD Read & Search (GET)**: `employee_list(request)` handling `?search=` filters.
* **CRUD Create & Update (POST)**: `employee_create` and `employee_update` validating form input and calling `.save()`.
* **CRUD Delete**: `employee_delete` confirming and executing `.delete()`.
* **Session Tracking**: `session_demo` setting and reading custom `request.session` cookies.

In `myproject/urls.py`, we linked the app routing table:
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('employee/', include('employee.urls')),  # <-- Routed employee module
]
```

### Step 6: Frontend Layout & Bootstrap 5 Integration (`templates/`)
We implemented a responsive design hierarchy using Django Template Language (DTL):
* **`base.html`**: Master layout loading Bootstrap 5 via CDN, global navigation bar, and flash message alert banners.
* **`home.html`**: Demonstrates variable injection (`{{ name }}`) and template inheritance (`{% extends 'employee/base.html' %}`).
* **`list.html`**: Displays dynamic data tables, search filters, and action buttons.
* **`form.html`**: Add/Edit employee form enforcing mandatory CSRF security (`{% csrf_token %}`).
* **`session_demo.html`**: Interactive testing ground for session storage cookies.

### Step 7: Static Files Loading (`static/`)
In `employee/static/css/style.css`, we added custom CSS hover animations and table styling, linked in HTML templates via:
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

### Step 8: Database Seeding
To ensure immediate usability during live demos, we ran a Python seeding script populating 3 initial employee records (**John Doe**, **Jane Smith**, and **Alex Johnson**).

---

## 🖥️ 4. How to Run & Live Class Demonstration Guide

### ⚡ Quick Start Commands
1. **Activate Virtual Environment:**
   ```powershell
   d:\Django\venv\Scripts\activate
   ```
2. **Navigate to Project Folder:**
   ```powershell
   cd d:\Django\myproject
   ```
3. **Start Development Server:**
   ```powershell
   python manage.py runserver
   ```

### 🎯 Live Classroom Demo Endpoints
When the server is running at `http://127.0.0.1:8000/`, open your browser to show students these endpoints:

| Demo Topic / Feature | URL Endpoint | What to Explain to Students |
| :--- | :--- | :--- |
| **🏠 MVT & FBV Home** | [`http://127.0.0.1:8000/employee/`](http://127.0.0.1:8000/employee/) | Shows dynamic variable injection (`{{ name }}`), MVT flow, and static files styling. |
| **🏛️ Class-Based View** | [`http://127.0.0.1:8000/employee/cbv/`](http://127.0.0.1:8000/employee/cbv/) | Demonstrates OOP approach (`View.as_view()`) rendering the exact same template. |
| **📋 CRUD List & Search** | [`http://127.0.0.1:8000/employee/list/`](http://127.0.0.1:8000/employee/list/) | Shows `Employee.objects.all()`, GET query parameters (`?search=...`), and relational data tables. |
| **➕ Add Employee Form** | [`http://127.0.0.1:8000/employee/create/`](http://127.0.0.1:8000/employee/create/) | Shows POST form handling, validation checks, and the critical `{% csrf_token %}` tag. |
| **💾 Session Management** | [`http://127.0.0.1:8000/employee/session/`](http://127.0.0.1:8000/employee/session/) | Shows how `request.session['key'] = value` stores data across browser requests. |
| **🔐 Django Admin Portal**| [`http://127.0.0.1:8000/admin/`](http://127.0.0.1:8000/admin/) | Show automatic GUI management. *(Login with your superuser credentials)*. |
| **🎓 Module 2 Student Roster**| [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/) | Shows the Module 2 student list portal. |

---

## 🛢️ 5. MySQL Database Integration Guide (Slide 13 Demo)
By default, this repository uses SQLite (`db.sqlite3`) for instant zero-configuration local development. When demonstrating production enterprise integration with MySQL to students, follow these steps:

1. **Install MySQL Database Driver:**
   ```bash
   pip install mysqlclient
   # Alternative driver: pip install pymysql
   ```
2. **Update Database Settings in `myproject/settings.py`:**
   Comment out the SQLite block and replace with your MySQL credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'companydb',          # Your MySQL database name
           'USER': 'root',               # MySQL username
           'PASSWORD': 'your_password',  # MySQL password
           'HOST': 'localhost',          # Database host (or IP)
           'PORT': '3306',
       }
   }
   ```
3. **Create MySQL Database & Apply Migrations:**
   ```bash
   # In MySQL command line or phpMyAdmin: CREATE DATABASE companydb;
   python manage.py migrate
   ```

---

## 🌐 6. Cloud Deployment & Automatic Superuser (Render)
This repository is 100% production-ready for instant deployment on **[Render.com](https://render.com/)**!
* **1-Click Blueprint:** Includes a preconfigured [`render.yaml`](file:///d:/Django/render.yaml) and [`build.sh`](file:///d:/Django/myproject/build.sh) for zero-setup deployments with Gunicorn and WhiteNoise.
* **Automatic Admin Superuser:** Because Render Free Tier instances do not provide persistent interactive shell access and reset ephemeral SQLite files on restart, our automated script ([`myproject/create_superuser.py`](file:///d:/Django/myproject/create_superuser.py)) automatically checks and generates an admin account whenever your app deploys or boots up!
  * **Default Username:** `admin`
  * **Default Password:** `admin123`
  *(Can be customized via `ADMIN_USERNAME` and `ADMIN_PASSWORD` environment variables in your Render Dashboard).*

> 📖 **Want the step-by-step deployment and troubleshooting guide?**  
> Check out: **[`RENDER_DEPLOYMENT_GUIDE.md`](file:///d:/Django/RENDER_DEPLOYMENT_GUIDE.md)**!

---
*Created for Django Full-Stack Web Development Training by GuruCharan Tanneeru.*
