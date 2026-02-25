class Book:

    def __init__(self, title, author, isbn, is_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    # String representation of the object (equivalent to toString() in Java)
    def __str__(self):
        return f"{self.title} by {self.author} [{self.isbn}] {'Available' if self.is_available else 'Not available'}"

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print("Book borrowed successfully")
        else:
            print("Book is not available")

    def return_book(self):
        self.is_available = True
        print("Book returned successfully")

    # store a list of all borrowed books, then introduce is_popular() method that works when book has been borrowed more than 5 times
    def is_popular(self):
        return len(self.borrowed_books) > 5
    
    
my_book = Book('100 años de soledad', 'Gabriel Garcia M.', '123456789', True)
my_book.borrow_book()
my_book.return_book()

my_book2 = Book('El principito', 'Antoine de Saint-Exupéry', '987654321', False)
my_book3 = Book('Las aventuras de un viaje en el tiempo', 'H.G. Wells', '123456789', True)

books_list = [my_book, my_book2, my_book3]

for book in books_list:
    print(book)
    print('')
