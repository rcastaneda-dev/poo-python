from exceptions import UserNotFoundError, BookNotFoundError

class BookStore:
    def __init__(self, name) -> None:
        """Initialize the bookstore"""
        self.books = []
        self.name = name
        self.users = []

    @property
    def available_books(self):
        """Return a list of available books"""
        return [book for book in self.books if book.is_available]

    def add_book(self, book):
        """Add a book to the bookstore"""
        self.books.append(book)

    def find_user_by_id(self, user_id):
        """Find a user by ID"""
        for user in self.users:
            if user.id == user_id:
                return user
        raise UserNotFoundError(f"User {user_id} not found")

    def find_book_by_title(self, title):
        """Find a book by title"""
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundError(f"Book {title} not found")

    # static methods are used for utility functions that are related to the class but do NOT use any instance attributes
    # in this case, validate_isbn is a utility function that is related to the class but does NOT use any instance attributes
    @staticmethod
    def _validate_isbn(isbn):
        if len(isbn) != 13 or not isbn.isdigit():
            raise ValueError("ISBN must be 13 digits")
        return True