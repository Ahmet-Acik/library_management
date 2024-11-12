# library_management/member.py

from .borrowable import Borrowable

class Member(Borrowable):
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, title):
        book = library.find_book(title)
        if book and not book.is_borrowed:
            book.borrow_book()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {title}")
        else:
            print("Book is not available.")

    def return_book(self, library, title):
        book = library.find_book(title)
        if book and book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {title}")
        else:
            print(f"Book was not borrowed by {self.name}")

    def list_borrowed_books(self):
        for book in self.borrowed_books:
            print(f"Borrowed Book: {book.title}")