import json
from datetime import datetime
from bookstore import BookStore
from books import Book, PhysicalBook, DigitalBook
from students import Student
from teachers import Teacher

class Persistence:
    def __init__(self, file="bookstore.json") -> None:
        self.file = file

    # ── Book helpers ──────────────────────────────────────────────────────────

    def _serialize_book(self, book):
        # Exclude private/mangled attributes (e.g. _Book__borrowed_count)
        d = {k: v for k, v in book.__dict__.items() if not k.startswith('_')}
        d["type"] = type(book).__name__  # "PhysicalBook", "DigitalBook", or "Book"
        return d

    def _deserialize_book(self, data):
        book_type = data.pop("type", "Book")
        if book_type == "PhysicalBook":
            return PhysicalBook(**data)
        elif book_type == "DigitalBook":
            return DigitalBook(**data)
        return Book(**data)

    # ── User helpers ──────────────────────────────────────────────────────────

    def _serialize_user(self, user):
        d = {k: v for k, v in user.__dict__.items() if not k.startswith('_')}
        # Store borrowed_books as a list of ISBNs instead of Book objects
        d["borrowed_books"] = [book.isbn for book in user.borrowed_books]
        d["type"] = type(user).__name__  # "Student" or "Teacher"
        return d

    def _deserialize_user(self, data, books_by_isbn):
        # Resolve ISBN list back to Book objects before constructing the user
        borrowed_isbns = data.pop("borrowed_books", [])
        user_type = data.pop("type", "student")
        data.pop("books_limit", None)  # set by __init__, don't pass it in
        if user_type == "Student":
            user = Student(**data)
        else:
            user = Teacher(**data)
        user.borrowed_books = [books_by_isbn[isbn] for isbn in borrowed_isbns if isbn in books_by_isbn]
        return user

    # ── Public API ────────────────────────────────────────────────────────────

    def save_data(self, bookstore):
        data = {
            "name": bookstore.name,
            "books": [self._serialize_book(book) for book in bookstore.books],
            "users": [self._serialize_user(user) for user in bookstore.users],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
        }
        with open(self.file, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_data(self):
        with open(self.file, 'r', encoding="utf-8") as f:
            data = json.load(f)
            biblioteca = BookStore(data["name"])
            biblioteca.books = [self._deserialize_book(book) for book in data["books"]]
            # Build a lookup so users can reference their borrowed books by ISBN
            books_by_isbn = {book.isbn: book for book in biblioteca.books}
            biblioteca.users = [self._deserialize_user(user, books_by_isbn) for user in data["users"]]
            return biblioteca