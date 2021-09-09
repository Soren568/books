from flask_app.config.mysqlconnection import connectToMySQL

# ! KeyError: 'title' when clicking on author 

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        result = connectToMySQL('books_schema').query_db(query,data)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for b in results:
            books.append(cls(b))
        return books

    @classmethod
    def save_fav(cls, data):
        query = "INSERT INTO favorites (book_id, author_id) VALUES (%(book_id)s, %(author_id)s)"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_favorites(cls, data):
        query = "SELECT * FROM authors JOIN favorites ON authors.id = favorites.author_id  JOIN books ON favorites.book_id = books.id WHERE books.id = %(id)s"
        results = connectToMySQL('books_schema').query_db(query, data)
        book = cls(results[0])
        book.authors = []
        for author in results:
            author_data = {
                "id": author['id'],
                "created_at": author['created_at'],
                "updated_at": author['updated_at']
            }
            book.authors.append(author)
            print(author)
        return book

    @classmethod
    def get_nonfavorites(cls, data):
        query = "select * from authors where id not in (select authors.id from authors join favorites on author_id = authors.id where book_id = %(id)s);"
        results = connectToMySQL('books_schema').query_db(query, data)
        return results
