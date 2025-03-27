import datetime
from utils.db import get_db_connection

class LibrarySystem:
    def __init__(self,user):
        self.user =user
        
    def view_all_books(self):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM books")
        books = c.fetchall()
        conn.close()
        return books
    
    def view_available_books(self):
        conn = get_db_connection()
        c = conn.execute()
        c.execute("SELECT * FROM books WHERE is_available = 1")
        books = c.fetchall()
        conn.close()
        return books
    
    def borrow_books(self,book_id):
        conn = get_db_connection()
        c = conn.cursor()
        
        # Let's check if the book is available or not
        
        c.execute("SELECT * FROM books WHERE id = ? AND is_available = 1",(book_id,))
        book = c.fetchone()
        if not book:
            print("Book is not available or doesn't exist")
            conn.close()
            return 
        
        # Update book to unavailable
        c.execute("UPDATE books SET is_available = 0 WHERE id =?",(book_id,))
        
        # Create borrow record
        borrow_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO borrowed_books(user_id,book_id,borrow_date) VALUES (?,?,?)",(self.user.id,book_id,borrow_date))
        
        conn.commit()
        conn.close()
        print("Book borrowed successfully")
        
    def return_book(self,book_id):
        conn = get_db_connection()
        c = conn.cursor()
        
        #Check if the user has borrowed this book
        c.execute('''
            SELECT * FROM borrowed_books
            WHERE user_id = ? AND book_id = ? AND return_date IS NULL           
        ''',(self.user.id,book_id))
        record = c.fetchone()
        
        # if not re