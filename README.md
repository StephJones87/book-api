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

## 🧙 A Gentle Story for First-Time API Builders

Imagine you’re building a **tiny library** in a quiet town. You want people to be able to ask what books are in stock, donate a new book, or remove one. You’re the librarian, and you decide to automate the whole thing. Here's how your system works:

### 🛖 `main.py` = The Library Front Door
This is where people come to make requests — “What books do you have?”, “Can I donate this one?”  
You hang up signs on the door like `@app.get("/books")` that tell people what questions they can ask. This is your **public interface**.

### 📘 `models.py` = Your Ledger
Inside the library, you have a **big ledger** where you log every book.  
You write down the **title**, **author**, and **a unique ID** for each one. This file defines what a “book” looks like in your world.

### 🛠️ `crud.py` = The Librarian’s Toolkit
When a request comes in — say, “add a book” or “remove book #3” — this file contains the tools and instructions to **do the actual work**.  
This is your toolkit of Create, Read, Update, and Delete commands (CRUD).

### 🧱 `database.py` = The Foundation
This sets up the **infrastructure** for your library — where the ledger is stored, how it opens and closes, and how records are written in.  
It’s your **storage engine and filing system**.

### 📦 `books.db` = The Bookshelf
This is where all the books live. It’s the **physical shelf** that holds your collection.  
You don’t touch it directly — you interact with it through your tools and front desk.

### 🎭 `BookCreate` (Pydantic) = The Intake Form
When someone donates a book, you hand them a form to fill in: "What’s the title? Who’s the author?"  
This form makes sure all new entries are **valid and clean** before they go on the shelf.

### 🚪 FastAPI + Uvicorn = Your Magical Building
FastAPI is the **building blueprint** — it tells people what the library can do.  
Uvicorn is the **electrical wiring and front gate** — it powers everything and lets people connect from outside.

So when someone walks up to your tiny automated library and says,  
> “Hello, show me all your books” —  
your system understands them, checks the shelf, and responds.
You’ve just built your first functioning digital library — powered by APIs

---
