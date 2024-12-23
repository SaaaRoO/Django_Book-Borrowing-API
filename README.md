# Library Management System Project

## Project Description

This Library Management System is a web-based application built using Django and Django REST Framework (DRF). It provides functionality for managing books and borrowing records while following clean architecture principles. The system is designed to support future enhancements and maintain scalability.

---

## Features

1. **User Management**:
   - Admin users can manage the system.
   - Authentication with session or token-based authentication.

2. **Book Management**:
   - Add, update, and delete book records.
   - List and search for available books.

3. **Borrowing System**:
   - Borrow and return books.
   - Track borrowed books and due dates.

4. **RESTful API**:
   - All functionality is exposed through a RESTful API for integration with other systems.

---

## Project Structure

```plaintext
library_system_project/
├── application/
│   ├── services/
│   ├── repositories/
│   └── ...
├── core/
│   └── ...
├── infrastructure/
│   └── ...
├── interfaces/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── tests/
│   └── test_*.py
├── library_system/
├── venv/
├── manage.py
├── db.sqlite3
└── README.md
```

---

## Installation

### Prerequisites

- Python 3.10 or later
- pip
- Virtualenv (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/SaaaRoO/Django_Book-Borrowing-API/tree/master
   cd library_system_project
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # For Linux/Mac
   venv\Scripts\activate     # For Windows
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

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application:
   Open a browser and navigate to `http://127.0.0.1:8000/`.

---

## API Endpoints

### Authentication
- `POST /api/auth/login/` - Login with credentials.
- `POST /api/auth/logout/` - Logout user.

### Books
- `GET /api/books/` - List all books.
- `POST /api/books/` - Add a new book.
- `PUT /api/books/{id}/` - Update book details.
- `DELETE /api/books/{id}/` - Delete a book.

### Borrowing
- `GET /api/borrowing/` - List all borrowed books.
- `POST /api/borrowing/` - Borrow a book.
- `PUT /api/borrowing/{id}/` - Return a borrowed book.

---

## Testing

### Run Tests

1. Ensure the virtual environment is activated.
2. Run the following command:
   ```bash
   python manage.py test
   ```

### Testing Using Postman

1. Import the provided Postman collection (`postman_collection.json`) into your Postman app.
2. Use the pre-configured endpoints to test the API functionality.

---

## Configuration

### Database

By default, the project uses SQLite. To switch to a different database (e.g., PostgreSQL):

1. Update the `DATABASES` section in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': '<db_name>',
           'USER': '<db_user>',
           'PASSWORD': '<db_password>',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
2. Install PostgreSQL dependencies:
   ```bash
   pip install psycopg2
   ```

### Static Files

To serve static files:

1. Configure `STATIC_URL` and `STATIC_ROOT` in `settings.py`:
   ```python
   STATIC_URL = '/static/'
   STATIC_ROOT = BASE_DIR / 'staticfiles'
   ```
2. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

---

## Contribution

1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Commit your changes and push them to your fork.
4. Create a pull request to the main branch.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- Built with [Django](https://www.djangoproject.com/) and [Django REST Framework](https://www.django-rest-framework.org/).
- Inspired by clean architecture principles.

