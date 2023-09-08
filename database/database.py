from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define your database connection URL. You can use SQLite for simplicity.
DATABASE_URL = "sqlite:///books.db"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a Session class to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
