from books import Book
from exceptions import InvalidTitleError

from abc import ABC, abstractmethod

class BaseUser(ABC):
    @abstractmethod
    def request_book(self, book):
        pass

class User(BaseUser):
    # main constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books : list[Book] = []

    def __str__(self):
        return f"User: {self.name} [{self.id}]"

    def request_book(self, book):
        if not book.title:
            raise InvalidTitleError("Book title is required")

        if self.books_limit is None or len(self.borrowed_books) < self.books_limit:
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{self.name} has reached the book limit")
