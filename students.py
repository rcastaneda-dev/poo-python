from users import User

class Student(User):
    def __init__(self, name, id, major):
        super().__init__(name, id)
        self.major = major
        self.books_limit = 3
        self.borrowed_books = []

    def __str__(self):
        return f"Student: {self.name} [{self.id}] [{self.major}]"

    def request_book(self, book):
        if len(self.borrowed_books) < self.books_limit:
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book}")
        else:
            print(f"{self.name} has reached the book limit")