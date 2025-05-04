# src/modules/movie.py

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "db", "movies.db")

def load_all_movies():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM movies")
    movies = c.fetchall()
    conn.close()
    return [dict(row) for row in movies]

def get_movie_by_title(title):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM movies WHERE Series_Title = ?", (title,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None
