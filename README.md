# CouchCritics

CouchCritics is a simple web-based movie review platform built with Flask and SQLite. It allows users to browse a collection of movies, view detailed information, register and log in, and submit reviews with ratings.

## Features

- User registration and login system
- Movie listing with pagination and search functionality
- Individual movie detail pages
- Authenticated users can submit reviews with a score and comment
- Reviews are stored in a database and displayed per movie

## Technologies Used

- Python 3
- Flask
- SQLite
- Bootstrap 5
- HTML (Jinja2 templating)

## Project Structure

project_root/
│
├── data/ # Source CSV file (for initial import)
├── src/
│ ├── app.py # Flask entry point
│ ├── db/
│ │ ├── movies.db # SQLite database
│ │ └── init_db.py # Script to create and populate database
│ ├── modules/ # Business logic (auth, movie, review)
│ ├── templates/ # HTML templates
│ └── static/ # Optional static assets
└── requirements.txt # Python dependencies
