from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# ==========================================
# MYSQL CONNECTION - XAMPP
# ==========================================
# XAMPP default MySQL:
# Username = root
# Password = empty
# Host = localhost
# Port = 3306
# Database = flask_blog

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:@localhost:3306/flask_blog"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# ==========================================
# POST MODEL
# ==========================================

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(
        db.String(200),
        nullable=False
    )

    content = db.Column(
        db.Text,
        nullable=False
    )

    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# ==========================================
# HOME - READ ALL POSTS
# ==========================================

@app.route("/")
def index():

    posts = Post.query.order_by(
        Post.timestamp.desc()
    ).all()

    return render_template(
        "index.html",
        posts=posts
    )


# ==========================================
# CREATE POST
# ==========================================

@app.route("/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":

        title = request.form["title"]
        content = request.form["content"]

        new_post = Post(
            title=title,
            content=content
        )

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("create.html")


# ==========================================
# EDIT POST
# ==========================================

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    post = Post.query.get_or_404(id)

    if request.method == "POST":

        post.title = request.form["title"]
        post.content = request.form["content"]

        db.session.commit()

        return redirect(url_for("index"))

    return render_template(
        "edit.html",
        post=post
    )


# ==========================================
# DELETE POST
# ==========================================

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):

    post = Post.query.get_or_404(id)

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("index"))


# ==========================================
# CREATE DATABASE TABLE
# ==========================================

with app.app_context():
    db.create_all()


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)
