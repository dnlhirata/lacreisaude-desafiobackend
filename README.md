# Desafio Backend - Lacrei Saúde
## Tech Stack
- Python 3.12
- Django 5.1
- Poetry

## How to run this project
First clone the project to a directory of your choice

### Setting up the environment
1. run `poetry install` inside the created folder. The command will create a virtual environment automatically and install all dependencies
2. run `poetry run python manage.py migrate` (when inside the directory that contains the `manage.py` file). This command will create the SQLite file and create the necessary tables
3. run `poetry run python manage.py runserver` to start the server

### Using the API
There two ways to test the API as it is right now: using the API Swagger UI or a tool like Postman or Insomnia
1. Browser (necessary to be logged in)
   1. Open the browser of you choice and navigate to `http://localhost:8000/api/docs`
2. Postman or Insomnia (or similar tools)
   1. Create a new request
   2. Set the request method and the correct URL
   3. Send request

## Architecture Decisions
### Django Framework
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It includes built-in features for user authentication, database management, and an admin interface.

### REST Framework (**djangorestframework**)
Provides powerful and flexible tools for building Web APIs, including serialization, authentication, and viewsets.

### API Documentation (**drf-spectacular**)
Simplifies the creation of OpenAPI 3.0 schema and provides a Swagger UI for API documentation.

### Database (**SQLite**)
Simple, file-based database suitable for development and testing. Can be easily replaced with more robust databases like PostgreSQL for production.

### Development Tools
- **ruff**: Configured in `pyproject.toml` for linting and code quality. Ensures code quality and consistency by enforcing coding standards.