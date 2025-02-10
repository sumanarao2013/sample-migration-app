# sample-migration-app
# Sample Migration App

A simple Flask application with SQLite database for demonstrating cloud migration strategies.

## Current Architecture
- Monolithic Flask application
- File-based SQLite database
- Basic containerization using Docker
- No load balancing
- No automatic scaling
- Local file storage

## Features
- REST API endpoints for user management
- Local SQLite database storage
- Docker support for containerization
- Basic user CRUD operations

## API Endpoints
- GET /users - Retrieve all users
- POST /users - Create a new user

## Local Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`

## Docker Setup
1. Build the image: `docker build -t sample-migration-app .`
2. Run the container: `docker run -p 5000:5000 sample-migration-app`

## Migration Needs
- Database needs to be moved to a cloud-managed service
- Application needs auto-scaling capabilities
- Requires proper logging and monitoring
- Needs secure secret management
- Requires proper CI/CD pipeline
