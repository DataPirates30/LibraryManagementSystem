from utils.db import get_db_connection

# This module does login/register the user(student/librarian)

# Register an user
def register_user(name,role,password):
    conn = get_db_connection()
    c = conn.cursor()
    
    # Check if user already exists
    
    c.execute("SELECT * FROM users WHERE name = ?",(name,))
    if c.fetchone():
        print(f"User {name} already exists.")
        conn.close()
        return False
    
    # Insert new user
    c.execute("INSERT INTO users(name,role,password) VALUES(?,?,?)",(name,role,password))
    conn.commit()
    conn.close()
    print(f"Registered {role} '{name}' successfully.")
    return True

# Login an existing user

def login_user(name,password):
    conn = get_db_connection()
    c = conn.cursor()
    
    c.execute("SELECT * FROM users WHERE name = ? AND password = ?",(name,password))
    user = c.fetchone()
    conn.close()
    
    if user:
        print(f"Login successful.Welcome {user[1]}")
        return user
    
    else:
        print("Invalid name or password")
        return None
    
    