from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.books import Book
from flask_app.models.authors import Author

@app.route('/')
def index():
    return redirect('/authors')


@app.route('/authors')
def authors():
    return render_template("authors.html", authors=Author.get_all())

@app.route('/save_author', methods=['POST'])
def save_author():
    Author.save(request.form)
    return redirect('/authors')


@app.route('/authors/<int:id>')
def author_favorites(id):
    data ={
        "id":id
    }
    return render_template("author_favorites.html", author = Author.get_one(data), nf = Author.get_nonfavorites(data))


@app.route('/books')
def books():
    return render_template("books.html", books=Book.get_all())

@app.route('/save_book', methods=['POST'])
def save_book():
    Book.save(request.form)
    return redirect('/books')


@app.route('/books/<int:id>')
def book_favorites(id):
    data = {
        "id":id
    }
    return render_template("book_favorites.html", book = Book.get_favorites(data), nf = Book.get_nonfavorites(data))

@app.route('/books/update', methods=['POST'])
def book_fav_update():
    Book.save_fav(request.form)
    return redirect(f"/books/{request.form['book_id']}")
