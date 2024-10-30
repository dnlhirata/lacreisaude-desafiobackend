# Desafio Backend - Lacrei Saúde
## Tech Stack
- Python 3.12
- Django 5.1
- Poetry

## How to run this project
First clone the project to a directory of your choice

### Setting up the environment
To set up the environment run `poetry install` inside the created folder. The command will create a virtual environment automatically and install all dependencies.

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