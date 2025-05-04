import sqlite3
import csv

# Veritabanını oluştur ve bağlan
conn = sqlite3.connect("movies.db")
c = conn.cursor()


# Movies tablosunu oluştur
c.execute("""
CREATE TABLE IF NOT EXISTS movies (
    Series_Title TEXT,
    Released_Year INTEGER,
    Certificate TEXT,
    Runtime INTEGER,
    Genre TEXT,
    IMDB_Rating REAL,
    Overview TEXT,
    Meta_score INTEGER,
    Director TEXT,
    Star1 TEXT,
    Star2 TEXT,
    Star3 TEXT,
    Star4 TEXT,
    No_of_Votes INTEGER,
    Gross INTEGER
)
""")

# Users tablosu
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Reviews tablosu
c.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    movie_title TEXT NOT NULL,
    score INTEGER NOT NULL,
    comment TEXT NOT NULL,
    date TEXT NOT NULL
)
""")

# CSV'den movie verilerini oku ve ekle
inserted, skipped = 0, 0
try:
    with open("../../data/movies.csv", newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                c.execute("""
                    INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    row["Series_Title"].strip(),
                    int(row["Released_Year"]),
                    row["Certificate"].strip(),
                    int(row["Runtime"]),
                    row["Genre"].strip(),
                    float(row["IMDB_Rating"]),
                    row["Overview"].strip(),
                    int(row["Meta_score"]) if row["Meta_score"].isdigit() else None,
                    row["Director"].strip(),
                    row["Star1"].strip(),
                    row["Star2"].strip(),
                    row["Star3"].strip(),
                    row["Star4"].strip(),
                    int(row["No_of_Votes"]),
                    int(row["Gross"]) if row["Gross"].isdigit() else None
                ))
                inserted += 1
            except Exception as e:
                skipped += 1
                continue
except FileNotFoundError:
    print("❌ CSV dosyası bulunamadı: data/movies.csv")
    conn.close()
    exit()

# Kapat
conn.commit()
conn.close()
print(f"✅ movies.db başarıyla oluşturuldu.")
print(f"✔ {inserted} satır eklendi, ❌ {skipped} satır atlandı.")
