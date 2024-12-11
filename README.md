# Todo App - FastAPI

This is a simple Todo application built using FastAPI. It allows users to manage their tasks effectively by performing CRUD (Create, Read, Update, Delete) operations.

## Features

- Create a new Todo
- Retrieve all Todos
- Retrieve a single Todo by ID
- Update an existing Todo
- Delete a Todo

## Requirements

- Python 3.7+
- FastAPI
- SQLAlchemy
- Uvicorn (for running the server)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/devazizov/todo-app-fastapi.git
   cd todo-app-fastapi
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   - Configure the database connection in `database/config.py`.

## Running the Application

Start the server using Uvicorn:

```bash
uvicorn main:app --reload
```

Start the server using FastAPI (dev or run):
```bash
fastapi dev main.py
```

The application will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Endpoints

### Todos

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| POST   | `/todo`         | Create a new Todo        |
| GET    | `/todo`         | Retrieve all Todos       |
| GET    | `/todo/{id}`    | Retrieve a Todo by ID    |
| PUT    | `/todo/{id}`    | Update a Todo by ID      |
| DELETE | `/todo/{id}`    | Delete a Todo by ID      |

### Example Todo Object

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, Eggs, Bread",
  "done": false
}
```

## Project Structure

```
.
├── database             # Database configuration and ORM
│   ├── config.py        # Database settings
│   ├── models.py        # Database models
│   └── orm.py           # ORM helper functions
├── index.html           # Static file (if applicable)
├── main.py              # Entry point of the application
├── routes               # API routes
│   ├── __init__.py      # Route initialization
│   ├── index.py         # Home route
│   └── todo.py          # Todo operations
├── schemas              # Pydantic schemas
│   └── todo.py          # Schemas for Todo
├── sql_todo.db          # SQLite database file
└── requirements.txt     # Python dependencies
```

## Example Requests

### Create a Todo

```bash
curl -X POST "http://127.0.0.1:8000/todo" \
-H "Content-Type: application/json" \
-d '{"title": "Learn FastAPI", "description": "Understand how FastAPI works", "done": false}'
```

### Retrieve All Todos

```bash
curl -X GET "http://127.0.0.1:8000/todo"
```

### Update a Todo

```bash
curl -X PUT "http://127.0.0.1:8000/todo/1" \
-H "Content-Type: application/json" \
-d '{"title": "Learn FastAPI Framework", "done": true}'
```

### Delete a Todo

```bash
curl -X DELETE "http://127.0.0.1:8000/todo/1"
```
### Author
[Check my website](https://azizov.dev)
