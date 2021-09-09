from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.books import Book


class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        result = connectToMySQL('books_schema').query_db(query,data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for a in results:
            authors.append(cls(a))
        return authors


    @classmethod
    def get_one(cls, data):
        print(data)
        query = "SELECT * FROM authors JOIN favorites ON authors.id = favorites.author_id JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query, data)
        # print(results)
        # print(type(results))
        author = cls(results[0])
        author.books = []
        for book in results:
            book_data = {
                "id": book["books.id"],
                "title": book["title"],
                "num_of_pages": book["num_of_pages"],
                "created_at": book["books.created_at"],
                "updated_at": book["books.updated_at"]
            }
            print(book)
            author.books.append(Book(book_data))
        return author

    @classmethod
    def get_nonfavorites(cls, data):
        query = "select * from books where id not in (select books.id from books join favorites on book_id = books.id where author_id = %(id)s);"
        results = connectToMySQL('books_schema').query_db(query, data)
        return results
