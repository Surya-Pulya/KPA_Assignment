

# FastAPI Bogie & Wheel Specification Project

## Project Overview

This project is a FastAPI-based backend for submitting and storing bogie checksheet forms and wheel specification forms. It uses SQLAlchemy ORM for database interactions and Pydantic for data validation.
Updated postman collection: https://surya-7134606.postman.co/workspace/17789742-8d98-44a2-8088-794a92a1c964/collection/45153103-06c29d34-1f52-4e94-9cf1-b370da1815da?action=share&source=copy-link&creator=45153103

Project demo: https://drive.google.com/file/d/1YQJMbwWXsl5CAgXMuNGfH9uHED5gH8Lb/view?usp=drive_link

## Setup Instructions
### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

- **Windows:**
  ```bash
  .venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source .venv/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

### 5. Run the Application

```bash
uvicorn python_test.main:app --reload
```

- The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Interactive docs(swaggerUI): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Key Features

- **Bogie Checksheet Submission:**  
  Submit bogie checksheet forms with nested details and validation.

- **Wheel Specification Submission:**  
  Submit wheel specification forms with detailed fields.

- **Database Integration:**  
  Uses SQLAlchemy ORM for SQLite database storage.

- **Error Handling:**  
  Returns HTTP 400 errors with details if form creation fails.

- **Pydantic Validation:**  
  All incoming data is validated using Pydantic schemas.

---

## Limitations & Assumptions

- **Database:**  
  Uses SQLite for simplicity. For production, configure a more robust database and use Alembic for migrations.

- **Migrations:**  
  No automatic migrations. If you change models, you must delete the SQLite file or use Alembic.

- **Data Model:**  
  Assumes the provided JSON structure for forms. Any changes to the schema require updates to both models and Pydantic schemas.

---

## Assumptions

- The user has Python 3.8+ installed.
- The project is run in a development environment.
- The database is recreated if models are changed.
