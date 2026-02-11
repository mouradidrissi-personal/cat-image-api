# 🐱 Cat Image API

A simple Flask and FastAPI application that displays random cat images using the Cat API.

## Features

- Display random cat images
- Built with both Flask and FastAPI
- Simple, clean UI
- RESTful API endpoints
- Health check endpoints

## Prerequisites

- Python 3.8+
- pip

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd cat-image-api
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Get a free API key from [The Cat API](https://thecatapi.com):
   - Sign up for a free account
   - Copy your API key

5. Create a `.env` file:
```bash
cp .env.example .env
# Edit .env and add your API key
```

## Usage

### Running Flask

```bash
python flask_app.py
```

Visit http://localhost:5000 in your browser.

### Running FastAPI

```bash
uvicorn fastapi_app:app --reload
```

Visit http://localhost:8000 in your browser.

API documentation available at:
- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)

## API Endpoints

### Flask

- `GET /` - Main page with cat images
- `GET /api/cats` - Get 10 random cat images
- `GET /api/cats/<count>` - Get specific number of cat images (1-25)
- `GET /health` - Health check

### FastAPI

- `GET /` - Main page with cat images
- `GET /api/cats` - Get random cat images (default: 10, max: 25)
- `GET /health` - Health check
- `GET /docs` - Interactive API documentation

## Example Requests

```bash
# Get 10 cat images (Flask)
curl http://localhost:5000/api/cats

# Get 5 cat images (Flask)
curl http://localhost:5000/api/cats/5

# Get 15 cat images (FastAPI)
curl http://localhost:8000/api/cats?count=15

# Health check
curl http://localhost:8000/health
```

## Project Structure

```
cat-image-api/
├── flask_app.py          # Flask application
├── fastapi_app.py        # FastAPI application
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
└── README.md            # This file
```

## License

MIT License

## Credits

- [The Cat API](https://thecatapi.com) - Free API for cat images