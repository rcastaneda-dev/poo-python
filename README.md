# CST BookStore (OOP Python)

A simple, Object-Oriented bookstore management system written in Python with JSON persistence.

## 🚀 Features

- **Book Management**: Support for different book types (`PhysicalBook`, `DigitalBook`).
- **User Management**: Different user types (`Student`, `Teacher`) with specific borrowing limits.
- **Persistence**: Save and load the entire bookstore state (books, users, and borrowing history) to/from a JSON file.
- **Exceptions**: Custom error handling for common bookstore scenarios.

## 📂 Project Structure

- `main.py`: The entry point of the application. It handles user interaction and seeds initial data if necessary.
- `bookstore.py`: Contains the `BookStore` class, which manages the collections of books and users.
- `books.py`: Defines the `Book` base class and its specialized subclasses (`PhysicalBook`, `DigitalBook`).
- `users.py`, `students.py`, `teachers.py`: Define the user hierarchy and specific behavior for students and teachers.
- `persistence.py`: Manages saving and loading the bookstore state to `bookstore.json`.
- `data.py`: Contains initial seed data for users and books.
- `exceptions.py`: Custom exceptions like `BookNotAvailableError` and `UserNotFoundError`.

## 🛠️ Usage

Simply run the main script to start the application:

```bash
python main.py
```

On first run, it will seed data from `data.py`. Subsequent runs will load the state from `bookstore.json`.

## 🧠 Key Concepts & Logic

- **Inheritance & Polymorphism**: Used for both books and users to share common behavior while allowing specialized functionality.
- **Encapsulation**: Using private attributes (e.g., `__borrowed_count`) and properties to protect internal state.
- **Custom Serialization**: The `Persistence` class handles converting complex objects (including circular references like borrowed books) into a JSON-compatible format by storing ISBN references.
- **Naming Conventions**: Internal helpers use the `_` prefix (e.g., `_serialize_book`) to distinguish them from the public API.
