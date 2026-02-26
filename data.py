from students import Student
from teachers import Teacher
from books import PhysicalBook, DigitalBook

# ─── Users ────────────────────────────────────────────────────────────────────
users = [
    Student("Carlos Méndez",      "STU-1001", "Computer Science"),
    Student("María González",     "STU-1002", "Literature"),
    Student("Andrés Ramírez",     "STU-1003", "History"),
    Student("Valeria Torres",     "STU-1004", "Mathematics"),
    Student("Diego Hernández",    "STU-1005", "Physics"),
    Student("Sofía Martínez",     "STU-1006", "Biology"),
    Student("Lucía Flores",       "STU-1007", "Philosophy"),
    Teacher("Dr. Roberto Vargas", "TCH-2001", "Computer Science"),
    Teacher("Dra. Elena Ríos",    "TCH-2002", "Literature"),
    Teacher("Dr. Javier Morales", "TCH-2003", "History"),
]

# ─── Books ────────────────────────────────────────────────────────────────────
books = [
    PhysicalBook(
        title        = "Cien años de soledad",
        author       = "Gabriel García Márquez",
        isbn         = "978-0-06-088328-7",
        is_available = True,
        publisher    = "Editorial Sudamericana",
        pages        = 471,
    ),
    PhysicalBook(
        title        = "El señor de los anillos",
        author       = "J.R.R. Tolkien",
        isbn         = "978-0-618-64015-7",
        is_available = True,
        publisher    = "Minotauro",
        pages        = 1178,
    ),
    PhysicalBook(
        title        = "1984",
        author       = "George Orwell",
        isbn         = "978-0-452-28423-4",
        is_available = True,
        publisher    = "Penguin Books",
        pages        = 328,
    ),
    PhysicalBook(
        title        = "Sapiens: De animales a dioses",
        author       = "Yuval Noah Harari",
        isbn         = "978-84-9992-351-0",
        is_available = True,
        publisher    = "Debate",
        pages        = 504,
    ),
    PhysicalBook(
        title        = "El código Da Vinci",
        author       = "Dan Brown",
        isbn         = "978-0-307-47427-5",
        is_available = True,
        publisher    = "Doubleday",
        pages        = 454,
    ),
    DigitalBook(
        title        = "Clean Code",
        author       = "Robert C. Martin",
        isbn         = "978-0-13-235088-4",
        is_available = True,
        file_size    = 4200,   # KB
    ),
    DigitalBook(
        title        = "The Pragmatic Programmer",
        author       = "David Thomas & Andrew Hunt",
        isbn         = "978-0-13-595705-9",
        is_available = True,
        file_size    = 5800,
    ),
    DigitalBook(
        title        = "Design Patterns",
        author       = "Gang of Four",
        isbn         = "978-0-20-163361-5",
        is_available = False,
        file_size    = 7100,
    ),
    DigitalBook(
        title        = "Introduction to Algorithms",
        author       = "Thomas H. Cormen et al.",
        isbn         = "978-0-26-204630-5",
        is_available = True,
        file_size    = 12500,
    ),
    DigitalBook(
        title        = "Artificial Intelligence: A Modern Approach",
        author       = "Stuart Russell & Peter Norvig",
        isbn         = "978-0-13-604259-4",
        is_available = True,
        file_size    = 9800,
    ),
]
