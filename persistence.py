import json
from datetime import datetime

class Persistence:
    def __init__(self, file="bookstore.json") -> None:
        self.file = file

    def save_data(self, bookstore):
        data = {
            "name": bookstore.name,
            "books": [book.__dict__ for book in bookstore.books],
            "users": [user.__dict__ for user in bookstore.users],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
        }
        with open(self.file, 'w', encoding="utf-8") as f:
            # grabs a dictionary and writes it to a file
            json.dump(data, f, indent=4, ensure_ascii=False)