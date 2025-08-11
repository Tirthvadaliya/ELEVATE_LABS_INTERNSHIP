# User Management REST API

This Python script (`demo.py`) implements a simple RESTful API for managing users using Flask. It supports basic CRUD operations (Create, Read, Update, Delete) for user data.

## Features

- List all users
- Retrieve a user by ID
- Create a new user (with name and email)
- Update an existing user's details
- Delete a user

## Requirements

- Python 3.x
- [Flask](https://pypi.org/project/Flask/)
- [Flask-RESTful](https://pypi.org/project/Flask-RESTful/)

Install dependencies with:
```sh
pip install flask flask-restful
```

## Usage

1. Run the script:
   ```sh
   python demo.py
   ```
2. The API will be available at `http://127.0.0.1:5000/`.

### Example Endpoints

- `GET /users` — List all users
- `GET /users/<user_id>` — Get user by ID
- `POST /users` — Create a new user (JSON: `{ "name": "...", "email": "..." }`)
- `PUT /users/<user_id>` — Update user (JSON: `{ "name": "...", "email": "..." }`)
- `DELETE /users/<user_id>` — Delete user

## File Structure

- `demo.py` : Main Flask REST API script
- `output/` : Folder containing screenshots for CRUD operations
- `README.md` : This documentation

> **Note:** Screenshots demonstrating CRUD operations are saved in the `output` folder.
