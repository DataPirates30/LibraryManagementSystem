class Library:
    books = []

    def __init__(self, name):
        self.name = name

    def add_book(self, book):
        Library.books.append(book)

    def remove_book(self, book):
        Library.books.remove(book)

    @classmethod
    def total_books(cls):
        return len(cls.books)

    @staticmethod
    def is_open(day):
        return day.lower() != 'sunday'
