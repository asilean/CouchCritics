# src/app.py

from flask import Flask, render_template, request, redirect, url_for, session
from modules.movie import load_all_movies, get_movie_by_title
from modules.review import get_reviews_for_movie, add_review
from modules.auth import register_user, login_user

app = Flask(__name__)
app.secret_key = "supersecretkey"  # I will change this to a random secret key.

# -------------- ROUTES --------------------

@app.route("/")
def index():
    query = request.args.get("q", "").strip().lower()
    all_movies = load_all_movies()

    if query:
        all_movies = [m for m in all_movies if query in m["Series_Title"].lower()]

    # Pagination
    page = int(request.args.get("page", 1))
    per_page = 9
    total = len(all_movies)
    total_pages = (total + per_page - 1) // per_page
    start = (page - 1) * per_page
    end = start + per_page
    paginated = all_movies[start:end]

    return render_template("index.html", movies=paginated, page=page, total_pages=total_pages, query=query)

@app.route("/movie/<title>", methods=["GET", "POST"])
def movie_detail(title):
    movie = get_movie_by_title(title)
    if not movie:
        return "Movie not found", 404

    user = session.get("user")

    if request.method == "POST":
        if not user:
            return "You must be logged in to review", 403
        score = int(request.form["score"])
        comment = request.form["comment"]
        add_review(user, title, score, comment)
        return redirect(url_for("movie_detail", title=title))

    reviews = get_reviews_for_movie(title)
    return render_template("movie_detail.html", movie=movie, reviews=reviews, user=user)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if login_user(username, password):
            session["user"] = username
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if register_user(username, password):
            session["user"] = username
            return redirect(url_for("index"))
        else:
            return render_template("register.html", error="Username already exists")
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))

# -------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
