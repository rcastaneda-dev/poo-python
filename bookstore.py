from exceptions import UserNotFoundError, BookNotFoundError

class BookStore:
    def __init__(self, name) -> None:
        """Initialize the bookstore"""
        self.books = []
        self.name = name
        self.users = []

    def available_books(self):
        """Return a list of available books"""
        return [book.title for book in self.books if book.is_available]

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