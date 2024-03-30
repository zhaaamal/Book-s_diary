from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db, init_db
from models import Book
from fastapi.staticfiles import StaticFiles
from data_management import router as data_router

app = FastAPI()

app.include_router(data_router)

# Подключение статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.on_event("startup")
async def startup_event():
    init_db()


@app.post("/books/{book_id}/favorites")
def add_book_to_favorites(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    # Добавить книгу в избранное
    # ...
    return {"message": "Книга добавлена в избранное"}


@app.delete("/books/{book_id}/favorites")
def remove_book_from_favorites(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    # Удалить книгу из избранного
    # ...
    return {"message": "Книга удалена из избранного"}
