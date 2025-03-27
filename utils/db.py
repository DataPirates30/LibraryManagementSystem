import sqlite3

# Connect to the database, create if not exists

def get_db_connection():
    conn = sqlite3.connect("library.db")
    return conn

# Initializing the database with the necessary tables

def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    
    # Creating users table
    
    c.execute(
        '''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT CHECK(role IN ('student','librarian')) NOT NULL,
            password TEXT NOT NULL
        )
        '''
    )
    
    # Creating books table
    
    c.execute(
        '''
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            is_available INTEGER DEFAULT 1   
        )
        '''
    )
    
    # Creating borrowed books table
    
    c.execute(
        '''
        CREATE TABLE IF NOT EXISTS borrowed_books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            book_id INTEGER,
            borrow_data TEXT,
            return_date TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(book_id) REFERENCES books(id)
        )
        '''    
    )
    
    conn.commit()
    conn.close()