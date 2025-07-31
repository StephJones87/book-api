# 📚 Book API with FastAPI + SQLite

This is a simple, beginner-friendly REST API for managing books.  
It uses **FastAPI** for the web framework and **SQLite** for local database storage.

---

## 🚀 Features

- ✅ View all books
- ✅ Get a book by ID
- ✅ Add a new book
- ✅ Delete a book
- 🧪 Interactive Swagger UI docs at `/docs`

---

## 🗂 Project Structure

```
book-api/
├── app/
│   ├── main.py         # FastAPI app + endpoints
│   ├── database.py     # DB engine and session
│   ├── models.py       # SQLAlchemy Book model
│   ├── crud.py         # Create, Read, Delete logic
├── books.db            # (Ignored) SQLite DB file
├── requirements.txt    # Python dependencies
├── .gitignore
├── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the repo:**

```bash
git clone https://github.com/YOUR-USERNAME/book-api.git
cd book-api
```

2. **Create a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the server:**

```bash
uvicorn app.main:app --reload
```

5. **Open the interactive docs:**

Visit 👉 http://127.0.0.1:8000/docs

---

## 🧪 Example Endpoints

### `GET /books`
Returns all books in the database.

### `POST /books`
Adds a new book. Example payload:
```json
{
  "title": "1984",
  "author": "George Orwell"
}
```

### `GET /books/{id}`
Returns one book by ID.

### `DELETE /books/{id}`
Deletes a book by ID.

---

## 📦 Built With

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLite](https://sqlite.org/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Uvicorn](https://www.uvicorn.org/)

---

## 🧠 Inspiration

This project was built to help me understand:
- How APIs are structured
- What happens between code and a database
- How to use FastAPI, SQLAlchemy, and Uvicorn together

---

## 🛡️ License

MIT — use freely, modify, and share.
