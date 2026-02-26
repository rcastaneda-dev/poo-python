from users import User

class Teacher(User):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department
        self.books_limit = None

    def __str__(self):
        return f"Teacher: {self.name} [{self.id}] [{self.department}]"
