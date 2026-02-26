from typing import Protocol

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

    def __init__(self, title, author, isbn, is_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available
        self.__borrowed_count = 0 # double underscore indicates that the variable is private

    # String representation of the object (equivalent to toString() in Java)
    def __str__(self):
        return f"{self.title} by {self.author} [{self.isbn}] {'Available' if self.is_available else 'Not available'}"

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            self.__borrowed_count += 1
            print(f"Book borrowed successfully {self.__borrowed_count} times")
        else:
            print("Book is not available")

    def return_book(self):
        self.is_available = True
        print("Book returned successfully")

    # store a list of all borrowed books, then introduce is_popular() method that works when book has been borrowed more than 5 times
    def is_popular(self):
        return self.__borrowed_count > 5

    def get_borrowed_count(self):
        return self.__borrowed_count

    def set_borrowed_count(self, count):
        if count > 0:
            self.__borrowed_count = count
        else:
            print("Borrowed count must be greater than 0")

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

