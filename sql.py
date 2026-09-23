import sqlite3

class Database:

    def __init__(self):
        self.connection = sqlite3.connect("movie_DB.db")
        self.cursor = self.connection.cursor()

    def add_movie(self, name, author, year, genre, rating):
        self.cursor.execute("INSERT INTO movies (name, author, year, genre, rating) VALUES (?, ?, ?, ?, ?)",(name, author, year, genre, rating))
        self.connection.commit()

    def get_movies(self):
        self.cursor.execute("SELECT * FROM movies")
        return self.cursor.fetchall()

    def edit_movie(self, id, name, author, year, genre, rating):
        self.cursor.execute("UPDATE movies SET name=?, author=?, year=?, genre=?, rating=? WHERE id=?",(name, author, year, genre, rating, id))
        self.connection.commit()

    def delete_movie(self, id):
        self.cursor.execute("DELETE FROM movies WHERE id=?",(id,))
        self.connection.commit()