class Library:
    def __init__(self):
        self.books = []
        self.authors = set()
        self.book_map = {}

    # Method to add a book to the library
    def add_book(self, book):
        self.books.append(book)
        self.authors.add(book.author)
        self.book_map[book.title] = book

    # Method to list all books in the library
    def list_books(self):
        for book in self.books:
            print(
                f"Title: {book.title}, Author: {book.author}, Borrowed: {book.is_borrowed}"
            )

    # Method to find a book by title
    def find_book(self, title):
        return self.book_map.get(title)

    # Method to borrow a book by title
    def borrow_book(self, title):
        book = self.find_book(title)
        if book:
            book.borrow_book()

    # Method to return a book by title
    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.return_book()

    # Method to get book by title
    def get_book(self, title):
        return self.find_book(title)

    # Method to get all books
    def get_books(self):
        return self.books

    # Method to get all authors
    def get_authors(self):
        return self.authors

    # Method to get books by author
    def get_books_by_author(self, author):
        return [book for book in self.books if book.author == author]

    # Method to get books by genre
    def get_books_by_genre(self, genre):
        return [book for book in self.books if book.genre == genre]

    # Method to get all available books
    def get_available_books(self):
        return [book for book in self.books if not book.is_borrowed]

    # Method to get all borrowed books
    def get_borrowed_books(self):
        return [book for book in self.books if book.is_borrowed]

    # Method to list all unique authors
    def list_authors(self):
        for author in self.authors:
            print(f"Author: {author}")
