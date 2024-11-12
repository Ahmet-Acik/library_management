# tests/test_library_management.py

import unittest
from library_management.book import Book
from library_management.library import Library
from library_management.member import Member

class TestLibraryManagement(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
        self.book2 = Book("1984", "George Orwell")
        self.book3 = Book("To Kill a Mockingbird", "Harper Lee")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.add_book(self.book3)
        self.member = Member("John Doe")

    def test_add_book(self):
        self.assertEqual(len(self.library.books), 3)

    def test_borrow_book(self):
        self.member.borrow_book(self.library, "1984")
        self.assertTrue(self.book2.is_borrowed)
        self.assertIn(self.book2, self.member.borrowed_books)

    def test_return_book(self):
        self.member.borrow_book(self.library, "1984")
        self.member.return_book(self.library, "1984")
        self.assertFalse(self.book2.is_borrowed)
        self.assertNotIn(self.book2, self.member.borrowed_books)

    def test_list_books(self):
        self.library.list_books()

    def test_list_authors(self):
        self.library.list_authors()

if __name__ == "__main__":
    unittest.main()