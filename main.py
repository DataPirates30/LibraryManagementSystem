from models.book import Book
from models.user import Student, Librarian
from models.library import Library

def run():
    lib = Library("City Library")

    book1 = Book("Python Basics", "John")
    book2 = Book("AI with Python", "Suman")

    lib.add_book(book1)
    lib.add_book(book2)

    student = Student("Alice", "S123")
    student.borrow_book(book1)

    print(student.get_role())  # Student
    for book in student.borrowed_books:
        print("Borrowed:", book)

    print("Open on Friday?", Library.is_open("Friday"))
    print("Total books:", Library.total_books())

if __name__ == "__main__":
    run()
