from books import Book, PhysicalBook, DigitalBook
from bookstore import BookStore
from data import users, books
from students import Student
from teachers import Teacher
from exceptions import InvalidTitleError, BookNotAvailableError, UserNotFoundError
from persistence import Persistence

# load data from file (seed from data.py if JSON doesn't exist yet)
persistence = Persistence()
try:
    biblioteca = persistence.load_data()
except FileNotFoundError:
    biblioteca = BookStore('Biblioteca Central')
    biblioteca.users = users
    biblioteca.books = books
    persistence.save_data(biblioteca)

print("Welcome to CST BookStore")
print("Available books:")
for book in biblioteca.available_books:
    print(f"- {book.complete_description}")

user_id = input("Enter user ID: ")

try:
    book_store_user = biblioteca.find_user_by_id(user_id)
    print(f"Welcome {book_store_user.name}")
    print(f"You have {book_store_user.books_limit} books limit")
    print(f"You have {len(book_store_user.borrowed_books)} books borrowed")
except UserNotFoundError as e:
    print(e)


book_title = input("Enter book title: ")

try:
    book_store_book = biblioteca.find_book_by_title(book_title)
    print(f"Book {book_store_book.title} found and is {'available' if book_store_book.is_available else 'not available'}")  
except BookNotFoundError as e:
    print(e)


book_store_user.request_book(book_store_book)

try:
    book_store_book.borrow_book()
except BookNotAvailableError as e:
    print(e)

# save data to file
persistence.save_data(biblioteca)

