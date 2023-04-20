'''
Create a new database named "films_db".
Use the SQLAlchemy library to create the database and tables in Python.
Part 1: Setting up the Database
Create one table for films, with the following columns:
    films table:
        id (integer, primary key)
        title (string)
        director (string)
        release year (integer)
Part 2: Manipulating with Database
    Create script that:
        Add 3 film to the film table.
        Update 1 film
        Print data from table
        Delete all data from table
'''
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    director = Column(String(255))
    release_year = Column(Integer)


engine = create_engine('sqlite:///films.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

film1 = Film(title='Inception', director='Christopher Nolan', release_year=2010)
film2 = Film(title='The Godfather', director='Francis Ford Coppola', release_year=1972)
film3 = Film(title='Pulp Fiction', director='Quentin Tarantino', release_year=1994)
session.add_all([film1, film2, film3])
session.commit()

# Update a film
film = session.query(Film).filter_by(title='Inception').first()
film.release_year = 2011
session.commit()

# Print data from the table
films = session.query(Film).all()
for film in films:
    print(f'Film Title: {film.title}, Director: {film.director}, Release Year: {film.release_year}')

# Delete all data from the table
session.query(Film).delete()
session.commit()