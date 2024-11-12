# library_management/library.py

class Library:
    def __init__(self):
        self.books = []
        self.authors = set()
        self.book_map = {}

    def add_book(self, book):
        self.books.append(book)
        self.authors.add(book.author)
        self.book_map[book.title] = book

    def list_books(self):
        for book in self.books:
            print(book)

    def find_book(self, title):
        return self.book_map.get(title)

    def get_available_books(self):
        return [book for book in self.books if not book.is_borrowed]

    def get_borrowed_books(self):
        return [book for book in self.books if book.is_borrowed]

    def list_authors(self):
        for author in self.authors:
            print(f"Author: {author}")