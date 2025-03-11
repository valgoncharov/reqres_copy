# reqres_copy

A FastAPI-based REST API that mimics some functionality of the reqres.in service. This project provides user data endpoints with a similar structure to reqres.in.

## Features

- RESTful API endpoints
- User data retrieval
- Pydantic models for data validation
- FastAPI automatic documentation

## Requirements

- Python 3.6+
- FastAPI
- Uvicorn
- Pydantic
- pytest (for testing)
- requests (for testing)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/reqres_copy.git
cd reqres_copy
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the server with:
```bash
python app.py
```

The server will start at `http://localhost:8000`

## API Endpoints

### GET /api/users/2

Returns user data for user ID 2.

Example response:
```json
{
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
    }
}
```

## Testing

Run tests using pytest:
```bash
pytest
```

## API Documentation

Once the server is running, you can access:
- Interactive API documentation (Swagger UI) at: `http://localhost:8000/docs`
- Alternative API documentation (ReDoc) at: `http://localhost:8000/redoc`