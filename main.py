from books import Book, PhysicalBook, DigitalBook
from bookstore import BookStore
from data import users, books
from students import Student
from teachers import Teacher
from exceptions import InvalidTitleError, BookNotAvailableError, UserNotFoundError

biblioteca = BookStore('Biblioteca Central')

# add users and books to bookstore
biblioteca.users = users
biblioteca.books = books

print("Welcome to CST BookStore")
print("Available books:")
for book in biblioteca.books:
    print(f"- {book.title}")

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
