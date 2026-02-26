class BookStore:
    def __init__(self, name) -> None:
        self.books = []
        self.name = name
        self.users = []

    def available_books(self):
        return [book.title for book in self.books if book.is_available]

    def add_book(self, book):
        self.books.append(book)
