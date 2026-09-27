import sqlite3
import logging
import os

# Get the exact folder where database.py is saved
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "payments.db")
def init_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor= conn.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS payments(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    event TEXT,
                    status TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )""")
        conn.commit()
        conn.close()
        print("Table created.")
    except Exception as e:
        logging.error(f"Error in creating table: {e}")

def update_payment_status(user_id, event):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor= conn.cursor()

        if event == "payment_success":
            status="paid"
        else :
            status="failed"
        
        cursor.execute("""INSERT INTO payments (user_id, event, status) VALUES (?,?,?) """,(user_id, event, status))
        conn.commit()
        conn.close()
        print(f"DB updated - User {user_id}: {status}")
    except Exception as e:
        logging.error(f"Error in Updating payment status: {e}")
        
        