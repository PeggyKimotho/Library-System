import click
from database.database import SessionLocal
from models.models import Author, Genre, Book

@click.command()
def add_author():
    """
    Add a new author to the library system.
    """
    name = click.prompt("Enter the author's name")

    db = SessionLocal()
    author = Author(name=name)
    db.add(author)
    db.commit()
    db.close()
    click.echo(f"Author '{name}' added successfully.")

@click.command()
def add_genre():
    """
    Add a new genre to the library system.
    """
    name = click.prompt("Enter the genre's name")

    db = SessionLocal()
    genre = Genre(name=name)
    db.add(genre)
    db.commit()
    db.close()
    click.echo(f"Genre '{name}' added successfully.")

@click.command()
def add_book():
    """
    Add a new book to the library system.
    """
    title = click.prompt("Enter the book's title")
    author_id = click.prompt("Enter the author's ID")
    genre_id = click.prompt("Enter the genre's ID")

    db = SessionLocal()
    book = Book(title=title, author_id=author_id, genre_id=genre_id)
    db.add(book)
    db.commit()
    db.close()
    click.echo(f"Book '{title}' added successfully.")

@click.command()
def list_books():
    """
    List all books in the library system.
    """
    db = SessionLocal()
    books = db.query(Book).all()

    if books:
        click.echo("Books in the library:")
        for book in books:
            # Access author and genre attributes within the active session
            db.refresh(book.author)  # Refresh author attribute
            db.refresh(book.genre)   # Refresh genre attribute
            click.echo(f"Title: {book.title}, Author: {book.author.name}, Genre: {book.genre.name}")
        db.close()
    else:
        db.close()
        click.echo("No books in the library.")

@click.command()
def list_authors():
    """
    List all authors in the library system.
    """
    db = SessionLocal()
    authors = db.query(Author).all()
    db.close()

    if authors:
        click.echo("Authors in the library:")
        for author in authors:
            click.echo(f"ID: {author.id}, Name: {author.name}")
    else:
        db.close()
        click.echo("No authors in the library.")

@click.command()
def list_genres():
    """
    List all genres in the library system.
    """
    db = SessionLocal()
    genres = db.query(Genre).all()
    db.close()

    if genres:
        click.echo("Genres in the library:")
        for genre in genres:
            click.echo(f"ID: {genre.id}, Name: {genre.name}")
    else:
        db.close()
        click.echo("No genres in the library.")

@click.group()
def main():
    """
    CLI for the library system/bookstore.
    """
    pass

# Add your CLI commands to the main group
main.add_command(add_author)
main.add_command(add_genre)
main.add_command(add_book)
main.add_command(list_books)
main.add_command(list_authors)
main.add_command(list_genres)

if __name__ == "__main__":
    main()
