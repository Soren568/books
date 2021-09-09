<!-- 1. KeyError: 'title' anytime I try to click on an author from /authors -->

<!-- 2. Book indexes are all out of order (book.id) on /book/<int:id> -->

<!-- 3. Dont know how to redirect to url that takes a book id as a parameter -->


# SQL QUERIES
```
SELECT * FROM authors 
LEFT JOIN favorites ON authors.id = favorites.author_id 
JOIN books ON favorites.book_id = books.id 
WHERE authors.id = 3;

SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE books.id = 3;

select * from books where id not in (select books.id from books join favorites on book_id = books.id where author_id = 1);
select * from authors where id not in (select authors.id from authors join favorites on author_id = authors.id where book_id = 1);

SELECT * FROM authors;
SELECT * FROM favorites;
SELECT * FROM books;

insert into favorites(book_id, author_id) values(3,4)
```