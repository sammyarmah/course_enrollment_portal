# EduTrack

A secure, role-based Course Enrollment Platform built with FastAPI, PostgreSQL, SQLAlchemy, Alembic, and JWT Authentication.

EduTrack provides a complete backend solution for managing courses, student enrollments, and administrative oversight while enforcing authentication, authorization, validation, and business rules.

---

## Features

### Authentication & Security

* JWT Authentication
* Secure password hashing
* Protected endpoints
* Role-Based Access Control (RBAC)
* Active user verification
* Secure dependency injection

### User Management

* User registration
* User login
* User profile retrieval
* Student and Admin roles
* Unique email validation

### Course Management

* View all active courses
* View course details
* Create courses (Admin only)
* Update courses (Admin only)
* Activate/Deactivate courses (Admin only)

### Enrollment Management

* Enroll in courses
* Deregister from courses
* Prevent duplicate enrollments
* Capacity validation
* Active course validation

### Administrative Oversight

* View all enrollments
* View enrollments by course
* Remove students from courses

### Database Features

* PostgreSQL database
* SQLAlchemy ORM
* Alembic migrations
* Entity relationships
* Repository pattern
* Service layer architecture

### Testing

* Automated API testing
* Authentication tests
* User management tests
* Course management tests
* Enrollment tests
* Administrative endpoint tests

---

## Tech Stack

| Technology | Purpose             |
| ---------- | ------------------- |
| FastAPI    | Web Framework       |
| PostgreSQL | Database            |
| SQLAlchemy | ORM                 |
| Alembic    | Database Migrations |
| JWT        | Authentication      |
| Passlib    | Password Hashing    |
| Pydantic   | Validation          |
| Pytest     | Testing             |
| Uvicorn    | ASGI Server         |

---

## Project Structure

```text
EduTrack/
│
├── alembic/
│   ├── versions/
│   └── env.py
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py
│   │       ├── users.py
│   │       ├── courses.py
│   │       └── enrollments.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   ├── deps.py
│   │   ├── db.py
│   │   └── db_async.py
│   │
│   ├── models/
│   │   ├── users.py
│   │   ├── courses.py
│   │   └── enrollments.py
│   │
│   ├── schemas/
│   │   ├── users.py
│   │   ├── courses.py
│   │   ├── enrollments.py
│   │   ├── auth.py
│   │   └── common.py
│   │
│   ├── repositories/
│   │   ├── user_repo.py
│   │   ├── course_repo.py
│   │   └── enrollment_repo.py
│   │
│   ├── services/
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── course.py
│   │   └── enrollment.py
│   │
│   └── main.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_users.py
│   ├── test_courses.py
│   └── test_enrollments.py
│
├── requirements.txt
├── alembic.ini
├── .env
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd EduTrack
```

### Create Virtual Environment

Windows:

```bash
python -m venv env
env\Scripts\activate
```

Linux/macOS:

```bash
python -m venv env
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
PROJECT_NAME=EduTrack

DATABASE_URL_ASYNC=your_async_database_url
DATABASE_URL_SYNC=your_sync_database_url

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

ENVIRONMENT=development
```

> Never commit `.env` files or sensitive credentials to version control.

---

## Database Setup

### Create Database

Create a PostgreSQL database before running migrations.

### Generate Migration

```bash
alembic revision --autogenerate -m "initial migration"
```

### Apply Migration

```bash
alembic upgrade head
```

### Rollback Migration

```bash
alembic downgrade -1
```

---

## Running the Application

Start the server:

```bash
uvicorn app.main:app --reload
```

Application:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```

---

## Authentication Flow

### Register

```http
POST /api/v1/auth/register
```

### Login

```http
POST /api/v1/auth/login
```

Returns:

```json
{
  "access_token": "jwt-token",
  "token_type": "bearer"
}
```

### Authorize in Swagger

1. Login
2. Copy the access token
3. Click Authorize in Swagger UI
4. Enter:

```text
Bearer <your_access_token>
```

5. Authorize

---

## Business Rules

### User Rules

* Email must be unique
* Role must be valid
* Inactive users cannot authenticate

### Course Rules

* Course code must be unique
* Capacity must be greater than zero
* Inactive courses cannot accept enrollments

### Enrollment Rules

* Only students can enroll
* Students cannot enroll twice in the same course
* Enrollment fails when capacity is reached
* Enrollment fails when course is inactive

---

## API Testing

Run all tests:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Run coverage:

```bash
pytest --cov=app
```

Generate coverage report:

```bash
pytest --cov=app --cov-report=html
```

---

## API Endpoints

### Authentication

| Method | Endpoint       | Access |
| ------ | -------------- | ------ |
| POST   | /auth/register | Public |
| POST   | /auth/login    | Public |

### Users

| Method | Endpoint  | Access        |
| ------ | --------- | ------------- |
| GET    | /users/me | Authenticated |

### Courses

| Method | Endpoint             | Access |
| ------ | -------------------- | ------ |
| GET    | /courses             | Public |
| GET    | /courses/{id}        | Public |
| POST   | /courses             | Admin  |
| PUT    | /courses/{id}        | Admin  |
| PATCH  | /courses/{id}/status | Admin  |

### Enrollments

| Method | Endpoint                           | Access  |
| ------ | ---------------------------------- | ------- |
| POST   | /enrollments                       | Student |
| DELETE | /enrollments/{course_id}           | Student |
| GET    | /enrollments                       | Admin   |
| GET    | /enrollments/course/{course_id}    | Admin   |
| DELETE | /enrollments/admin/{enrollment_id} | Admin   |

---

## Security Considerations

* Passwords are hashed before storage
* JWT authentication protects secured endpoints
* Role-based access control is enforced
* Input validation is handled using Pydantic
* Database interactions use SQLAlchemy ORM
* Sensitive configuration is stored in environment variables

---

## Future Enhancements

* Pagination and filtering
* Audit logging
* Soft deletes
* Rate limiting
* Email notifications
* Course prerequisites
* Refresh token authentication
* Docker support
* CI/CD pipeline

---

## License

This project was developed for educational purposes as part of a backend engineering assessment.

