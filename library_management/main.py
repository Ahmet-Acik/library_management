from library_management.book import Book
from library_management.library import Library
from library_management.member import Member
from library_management.borrowable import Borrowable


def main():
    # Create a library
    my_library = Library()

    # Add books to the library
    my_library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "Novel", 1925))
    my_library.add_book(Book("1984", "George Orwell", "Dystopian", 1949))
    my_library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "Novel", 1960))
    my_library.add_book(Book("Pride and Prejudice", "Jane Austen", "Novel", 1813))
    my_library.add_book(Book("Animal Farm", "George Orwell", "Political satire", 1945))
    my_library.add_book(Book("Brave New World", "Aldous Huxley", "Dystopian", 1932))
    my_library.add_book(Book("The Catcher in the Rye", "J.D. Salinger", "Novel", 1951))
    my_library.add_book(Book("Lord of the Flies", "William Golding", "Allegory", 1954))
    my_library.add_book(Book("The Grapes of Wrath", "John Steinbeck", "Novel", 1939))
    my_library.add_book(Book("Lord of the Rings", "J.R.R. Tolkien", "Fantasy", 1954))
    my_library.add_book(Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 1937))
    # Add some classic books
    my_library.add_book(
        Book("Crime and Punishment", "Fyodor Dostoevsky", "Philosophical novel", 1866)
    )
    my_library.add_book(Book("War and Peace", "Leo Tolstoy", "Historical novel", 1869))
    my_library.add_book(Book("Anna Karenina", "Leo Tolstoy", "Realist novel", 1877))
    my_library.add_book(Book("Moby-Dick", "Herman Melville", "Adventure novel", 1851))

    # List all books in the library
    print("Listing all books in the library:")
    my_library.list_books()

    # List all unique authors in the library
    print("\nListing all unique authors in the library:")
    my_library.list_authors()

    # Create a member
    member = Member("John Doe", True)

    # Member borrows a book
    print("\nJohn Doe borrows '1984':")
    member.borrow_book(my_library, "1984", True)

    # List all books in the library after borrowing
    print("\nListing all books in the library after borrowing:")
    my_library.list_books()

    # List all borrowed books by the member
    print("\nListing all borrowed books by John Doe:")
    member.list_borrowed_books()

    # List available books in the library
    print("\nListing available books in the library:")
    for book in my_library.get_available_books():
        print(f"Available Book: {book.title}")

    # List borrowed books in the library
    print("\nListing borrowed books in the library:")
    for book in my_library.get_borrowed_books():
        print(f"Borrowed Book: {book.title}")

    # Member returns a book
    print("\nJohn Doe returns '1984':")
    member.return_book(my_library, "1984")

    # List all books in the library after returning
    print("\nListing all books in the library after returning:")
    my_library.list_books()

    # List all borrowed books by the member after returning
    print("\nListing all borrowed books by John Doe after returning:")
    member.list_borrowed_books()

    # Member tries to borrow a book with inactive account
    print("\nJohn Doe tries to borrow '1984' with inactive account:")
    member = Member("John Doe", False)
    member.borrow_book(my_library, "1984", False)

    # List all borrowed books by the member after trying to borrow with inactive account
    print(
        "\nListing all borrowed books by John Doe after trying to borrow with inactive account:"
    )
    member.list_borrowed_books()

    # Member tries to return a book that was not borrowed
    print("\nJohn Doe tries to return '1984' that was not borrowed:")
    member.return_book(my_library, "1984")

    # Get books by author
    print("\nListing all books by George Orwell:")
    for book in my_library.get_books_by_author("George Orwell"):
        print(f"Book by George Orwell: {book.title}")

    # Get books by genre
    print("\nListing all Dystopian books:")
    for book in my_library.get_books_by_genre("Dystopian"):
        print(f"Dystopian Book: {book.title}")

    # Get available books
    print("\nListing all available books:")
    for book in my_library.get_available_books():
        print(f"Available Book: {book.title}")

    # Get borrowed books
    print("\nListing all borrowed books:")
    for book in my_library.get_borrowed_books():
        print(f"Borrowed Book: {book.title}")

    # Get book by title
    print("\nGetting book '1984':")
    book = my_library.find_book("1984")
    if book:
        print(f"Book found: {book.title}")
    else:
        print("Book not found.")

    # Get all books
    print("\nGetting all books:")
    for book in my_library.get_books():
        print(f"Book: {book.title}")

    # Get all authors
    print("\nGetting all authors:")
    for author in my_library.get_authors():
        print(f"Author: {author}")


if __name__ == "__main__":
    main()
