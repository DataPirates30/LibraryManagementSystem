from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name,ssid):
        self.name = name
        self.id = ssid

    @abstractmethod
    def get_role(self):
        pass

class Student(User):
    def __init__(self, name, student_id,phone_no):
        super().__init__(name,student_id)
        self.phone_no = phone_no
        self.borrowed_books = []

    def get_role(self):
        return "Student"

    def borrow_book(self, book):
        self.borrowed_books.append(book)

class Librarian(User):
    def get_role(self):
        return "Librarian"
