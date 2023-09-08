Introduction
The Library System/Bookstore project is a Command-Line Interface (CLI) application that allows you to manage a virtual library or bookstore. With this system, you can add authors, genres, and books to your collection and list all books, authors, and genres. It's a simple and efficient way to organize and keep track of your library's inventory.

Project Overview
This project consists of several key components:

CLI Interface (main.py): The main entry point of the application is the main.py file. It uses the Click library to create a user-friendly command-line interface for interacting with the library system.

Database (database.py): The database is powered by SQLAlchemy, and it's used to store information about authors, genres, and books. It is designed to work with a SQLite database, making it easy to set up and use.

Data Models (models.py): The data models define the structure of the database tables. In this project, there are three main models: Author, Genre, and Book. They are used to represent authors, genres, and books, and they have relationships with each other.

Data Seeding (seed.py): This script populates the database with initial sample data for authors, genres, and books. It's a convenient way to get started with the library system and see how it works.

Usage
To use the Library System/Bookstore, you can run various commands through the command-line interface. Here are some of the available commands:

Commands
add_author: Add a new author to the library system.
add_genre: Add a new genre to the library system.
add_book: Add a new book to the library system.
list_books: List all books in the library system.
list_authors: List all authors in the library system.
list_genres: List all genres in the library system.

To run a command, open a terminal, navigate to the project directory, activate the virtual environment (if used), and execute the desired command using python main.py <command>.

Project Structure
The project is structured as follows:

main.py: The main CLI application with all the commands.
database.py: Configuration for the SQLite database and the database session.
models.py: Data models for Author, Genre, and Book.
seed.py: A script to seed the database with initial data.
books.db: The SQLite database file (created after seeding).



