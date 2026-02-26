from books import Book, PhysicalBook, DigitalBook
from bookstore import BookStore

my_physical_book = PhysicalBook('100 años de soledad', 'Gabriel Garcia M.', '123456789', True, 'Random House', 1000)
my_second_physical_book = PhysicalBook('Not available book', 'Gabriel Garcia M.', '123456789', False, 'Random House', 1000)
my_digital_book = DigitalBook('100 años de soledad', 'Gabriel Garcia M.', '123456789', True, 1000)
biblioteca = BookStore('Biblioteca Central')
biblioteca.add_book(my_physical_book)
biblioteca.add_book(my_second_physical_book)
biblioteca.add_book(my_digital_book)

print(biblioteca.available_books())
