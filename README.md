# ReqRes API Clone

A FastAPI project that mimics reqres.in endpoints with additional features and improvements.

## Features

- **RESTful API Endpoints**
  - Get single user
  - List users with pagination
  - Create user
  - Update user
  - Delete user
  - Get user avatar

- **Advanced Features**
  - Request/Response logging
  - Rate limiting (60 requests per minute)
  - Input validation
  - Error handling
  - CORS support
  - Swagger documentation

## Project Structure

```
app/
├── api/
│   ├── endpoints/
│   │   └── users.py
│   ├── api.py
│   └── __init__.py
├── core/
│   ├── config.py
│   ├── exceptions.py
│   └── middleware.py
├── models/
│   ├── user.py
│   └── __init__.py
└── app.py
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/valgoncharov/reqres_copy.git
cd reqres_copy
```

2. Install dependencies using Poetry:
```bash
poetry install
```

## Running the Application

Start the server:
```bash
poetry run uvicorn app.app:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

- `GET /api/users/{user_id}` - Get a specific user
- `GET /api/users` - List users with pagination and filtering
- `POST /api/users` - Create a new user
- `PUT /api/users/{user_id}` - Update a user
- `DELETE /api/users/{user_id}` - Delete a user
- `GET /api/users/{user_id}/avatar` - Get user's avatar URL

### Query Parameters

- `page` - Page number (default: 1)
- `per_page` - Items per page (default: 6, max: 20)
- `email` - Filter users by email
- `name` - Filter users by first or last name

## Error Handling

The API includes proper error handling for:
- Not found resources
- Validation errors
- Rate limiting
- Bad requests

## Dependencies

- Python 3.8+
- FastAPI
- Pydantic
- Uvicorn
- Requests