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
    
    
my_book = Book('100 años de soledad', 'Gabriel Garcia M.', '123456789', True)
my_book.borrow_book()
my_book.return_book()
my_book.borrow_book()
my_book.return_book()

my_book2 = Book('El principito', 'Antoine de Saint-Exupéry', '987654321', False)
my_book3 = Book('Las aventuras de un viaje en el tiempo', 'H.G. Wells', '123456789', True)

books_list = [my_book, my_book2, my_book3]

for book in books_list:
    print(book)
    print('')

my_book.set_borrowed_count(10)
print(my_book.get_borrowed_count())