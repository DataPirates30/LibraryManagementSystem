from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,id,name):
        self.id = id
        self.name = name
        
    @abstractmethod
    def get_role(self):
        pass
    
    @abstractmethod
    def get_dashboard(self):
        pass

#Making the student class

class Student(User):
    def __init__(self,id,name):
        super().__init__(id,name)
        self.borrowed_books = []
    
    def get_role(self):
        return "Student"
    
    def get_dashboard(self):
        return [
            "1. View available books",
            "2. Borrow a book",
            "3. Return a book",
            "4. View my borrowed books"
        ] 
    
class Librarian(User):
    def __init__(self,id,name):
        super().__init_(id,name)
        
    def get_role(self):
        return "Student"

    def get_dashboard(self):
        return [
            "1. View available books",
            "2. Borrow a book",
            "3. Return a book",
            "4. View my borrowed books"
        ] 

        