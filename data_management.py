from fastapi import APIRouter, HTTPException
from database import SessionLocal
from models import Book, Comment

router = APIRouter()


@router.post("/books/")
def create_book(title: str, author: str, rating: float, comments: str):
    db = SessionLocal()
    book = Book(title=title, author=author, rating=rating, comments=comments)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


@router.get("/books/{book_id}")
def read_book(book_id: int):
    db = SessionLocal()
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Добавьте другие эндпоинты для обновления и удаления книг, а также для управления комментариями
