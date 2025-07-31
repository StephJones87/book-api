from sqlalchemy.orm import Session
from .models import Book

def get_books(db: Session):
    return db.query(Book).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, title: str, author: str):
    new_book = Book(title=title, author=author)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return True
    return False
