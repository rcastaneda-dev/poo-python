from users import User

class Student(User):
    # main constructor
    def __init__(self, name, id, major):
        super().__init__(name, id)
        self.major = major
        self.books_limit = 3
        self.borrowed_books = []

    # variant constructor for specific majors
    @classmethod
    def create_with_limit(cls, name, id, major="Computer Science", books_limit=5):
        return cls(name, id, major, books_limit)

    def __str__(self):
        return f"Student: {self.name} [{self.id}] [{self.major}]"

    def request_book(self, book):
        if len(self.borrowed_books) < self.books_limit:
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{self.name} has reached the book limit")