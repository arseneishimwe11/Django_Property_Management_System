# Property Management System

This Property Management System is a web application built with Django, designed to manage rental properties, tenants, and associated records efficiently. It includes modules for handling users, properties, and tenants, complete with CRUD functionality, relational data management, and an intuitive web interface.

---

### Project Structure

The project structure is organized into separate Django apps to keep code modular and maintainable:

- **Users**: Manages user accounts and profiles.
- **Properties**: Handles property records, such as addresses, descriptions, and availability.
- **Tenants**: Manages tenant information and leases, linking tenants to properties.

---

### Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Features](#features)
- [Usage](#usage)
- [Requirements](#requirements)

---

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/property-management-system.git
   cd property-management-system
   ```
2. **Set Up a Virtual Environment**
  
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Linux/Mac
   # or
   env\Scripts\activate  # On Windows
   ```
3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Apply Migrations**
  
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Linux/Mac
   # or
   env\Scripts\activate  # On Windows
   ```
5. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```
6.**Run the Development Server**

   ```bash
   python manage.py runserver
   ```

***Access the app in your browser at http://127.0.0.1:8000 ***

---

### Project Structure
Here's an overview of the main project files and directories

```plaintext
property_management/
├── property_management/  # Project configuration files
│   ├── settings.py       # Django settings
│   ├── urls.py           # Root URL configuration
│   └── wsgi.py           # WSGI configuration
├── users/                # Users app for managing accounts
├── properties/           # Properties app for managing property records
├── tenants/              # Tenants app for managing tenant information
├── templates/            # HTML templates for rendering views
├── manage.py             # Django command-line utility
└── requirements.txt      # Project dependencies
```

---

### Features

**User Management:** Create and manage user accounts and profiles.
**Property Management:** Record properties with details like addresses, descriptions, and availability.
**Tenant Management:** Manage tenant information, including lease records and linking tenants to properties.
**CRUD Functionality:** Each module supports full CRUD (Create, Read, Update, Delete) operations.
**Relational Data** Management: Link properties to tenants and manage these relationships.
**Authentication:** Secure login system for property managers.

---

### Usage
After setting up the server, access the Django admin panel at http://127.0.0.1:8000/admin to manage properties, tenants, and users. Use the Django interface to create, view, update, or delete records for each module.

**Login:** Use the superuser credentials created during setup.
**Manage Users:** Add or modify user accounts via the Users module.
**Add Properties:** Register new properties in the Properties module with relevant details.
**Assign Tenants:** Link tenants to properties through the Tenants module.

--- 

**Requirements**
- **Python 3.x**
- **Django 3.x+**
- **Database:** SQLite (default), can be configured for PostgreSQL or MySQL
- **Dependencies:** Listed in requirements.txt

*For additional customization, modify the configurations in settings.py, including database, email, and any other Django settings.*




