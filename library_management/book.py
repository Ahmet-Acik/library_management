# library_management/book.py


class Book:
    def __init__(self, title, author, genre, year, is_borrowed=False):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.is_borrowed = is_borrowed

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
        else:
            print("Book is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
        else:
            print("Book was not borrowed.")

    def __str__(self):
        return (
            f"Title: {self.title}, Author: {self.author}, Borrowed: {self.is_borrowed}"
        )
