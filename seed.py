from database.database import SessionLocal
from models.models import Author, Genre, Book

# Define sample data for authors, genres, and books 
authors_data = [
    {"name": "Charles Dickens"},
    {"name": "James Baldwin"},
    {"name": "Allan Moore"},
]

genres_data = [
    {"name": "Fiction"},
    {"name": "Biography"},
    {"name": "Comic"},
]

books_data = [
    {"title": "A Tale of Two Cities", "author_id": 1, "genre_id": 1},
    {"title": "Begin Again", "author_id": 2, "genre_id": 2},
    {"title": "Watchmen", "author_id": 3, "genre_id": 3},
]

def seed_database():
    db = SessionLocal()

    try:
        # Insert authors
        for author_data in authors_data:
            author = db.query(Author).filter_by(name=author_data["name"]).first()
            if author is None:
                author = Author(**author_data)
                db.add(author)

        # Insert genres
        for genre_data in genres_data:
            genre = db.query(Genre).filter_by(name=genre_data["name"]).first()
            if genre is None:
                genre = Genre(**genre_data)
                db.add(genre)

        # Insert books
        for book_data in books_data:
            book = db.query(Book).filter_by(title=book_data["title"]).first()
            if book is None:
                book = Book(**book_data)
                db.add(book)

        db.commit()
        print("Seed data inserted successfully.")
    except Exception as e:
        db.rollback()
        print(f"Error: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()