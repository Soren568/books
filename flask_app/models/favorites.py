from flask_app.config.mysqlconnection import connectToMySQL

class Favorite:
    def __init__(self, data):
        self.id = data['id']
        self.author_id = data['book_id']
        self.book_id = data['book_id']