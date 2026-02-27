from typing import Protocol
from exceptions import BookNotAvailableError, InvalidTitleError

class BookProtocol(Protocol):
    def borrow_book(self) -> str:
        """ Borrow a book """
        ...

    def return_book(self) -> str:
        """ Return a book """
        ...

    def calculate_duration(self) -> str:
        """ Calculate the duration of the book """
        ...


class Book: 

    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available
        self.__borrowed_count = 0 # double underscore indicates that the variable is private

    @classmethod
    def create_not_available(cls, title, author, isbn):
        return cls(title, author, isbn, is_available=False)

    # String representation of the object (equivalent to toString() in Java)
    def __str__(self):
        return f"{self.title} by {self.author} [{self.isbn}] {'Available' if self.is_available else 'Not available'}"

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            self.__borrowed_count += 1
            print(f"Book borrowed successfully {self.__borrowed_count} times")
        else:
            raise BookNotAvailableError(self.title)

    def return_book(self):
        self.is_available = True
        print("Book returned successfully")

    # store a list of all borrowed books, then introduce is_popular() property that works when book has been borrowed more than 5 times
    @property
    def is_popular(self):
        return self.__borrowed_count > 5

    @property
    def borrowed_count(self):
        return self.__borrowed_count

    @borrowed_count.setter
    def borrowed_count(self, count):
        if count > 0:
            self.__borrowed_count = count
        raise ValueError("borrowed_count must be greater than 0")

    @property
    def complete_description(self):
        return f"{self.title} by {self.author} [{self.isbn}]"

class PhysicalBook(Book):
    def __init__(self, title, author, isbn, is_available, publisher, pages):
        super().__init__(title, author, isbn, is_available)
        self.publisher = publisher
        self.pages = pages

    def calculate_duration(self):
        return "Physical 7 days"

class DigitalBook(Book):
    def __init__(self, title, author, isbn, is_available, file_size):
        super().__init__(title, author, isbn, is_available)
        self.file_size = file_size

    def calculate_duration(self):
        return "Digital 14 days"

