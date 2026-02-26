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
    print(f"- {book}")

user_id = input("Enter user ID: ")

try:
    book_store_user = biblioteca.find_user_by_id(user_id)
    print(f"Welcome {book_store_user.name}")
    print(f"You have {book_store_user.books_limit} books limit")
    print(f"You have {len(book_store_user.borrowed_books)} books borrowed")
except UserNotFoundError as e:
    print(e)

