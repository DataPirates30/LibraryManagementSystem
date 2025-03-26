from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

class Student(User):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
        self.borrowed_books = []

    def get_role(self):
        return "Student"

    def borrow_book(self, book):
        self.borrowed_books.append(book)

class Librarian(User):
    def get_role(self):
        return "Librarian"
