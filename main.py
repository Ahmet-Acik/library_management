# main.py

from library_management.book import Book
from library_management.library import Library
from library_management.member import Member

def main():
    # Create a library
    library = Library()

    # Add books to the library
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

    # List all books in the library
    print("Listing all books in the library:")
    library.list_books()

    # List all unique authors in the library
    print("\nListing all unique authors in the library:")
    library.list_authors()

    # Create a member
    member = Member("John Doe")

    # Member borrows a book
    print("\nJohn Doe borrows '1984':")
    member.borrow_book(library, "1984")

    # List all books in the library after borrowing
    print("\nListing all books in the library after borrowing:")
    library.list_books()

    # List all borrowed books by the member
    print("\nListing all borrowed books by John Doe:")
    member.list_borrowed_books()

    # List available books in the library
    print("\nListing available books in the library:")
    for book in library.get_available_books():
        print(f"Available Book: {book.title}")

    # List borrowed books in the library
    print("\nListing borrowed books in the library:")
    for book in library.get_borrowed_books():
        print(f"Borrowed Book: {book.title}")

    # Member returns a book
    print("\nJohn Doe returns '1984':")
    member.return_book(library, "1984")

    # List all books in the library after returning
    print("\nListing all books in the library after returning:")
    library.list_books()

    # List all borrowed books by the member after returning
    print("\nListing all borrowed books by John Doe after returning:")
    member.list_borrowed_books()

if __name__ == "__main__":
    main()