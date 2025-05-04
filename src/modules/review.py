# src/modules/review.py

import sqlite3
import os
from datetime import datetime

# Veritabanı dosyasının doğru yolu
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "db", "movies.db")

def add_review(username, title, score, comment):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Aynı kullanıcı aynı filme birden fazla yorum yapmasın
    c.execute("SELECT * FROM reviews WHERE username=? AND movie_title=?", (username, title))
    if c.fetchone():
        conn.close()
        return

    c.execute("""
        INSERT INTO reviews (username, movie_title, score, comment, date)
        VALUES (?, ?, ?, ?, ?)
    """, (username, title, score, comment, datetime.now().strftime("%Y-%m-%d %H:%M")))
    conn.commit()
    conn.close()

def get_reviews_for_movie(title):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM reviews WHERE movie_title = ?", (title,))
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]
