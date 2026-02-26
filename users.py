class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def __str__(self):
        return f"User: {self.name} [{self.id}]"

    def request_book(self, book):
        if self.books_limit is None or len(self.borrowed_books) < self.books_limit:
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book}")
        else:
            print(f"{self.name} has reached the book limit")


estudiante = Student("Juan", 1, "Computer Science")
profesor = Teacher("Pedro", 2, "Computer Science")
estudiante.request_book("Python")
estudiante.request_book("Python Medio")
estudiante.request_book("Python Avanzado")
estudiante.request_book("Python Expert")
profesor.request_book("Python")