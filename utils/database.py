"""Database helper functions for Civic Pulse complaint storage."""
import sqlite3
from datetime import datetime

DB_PATH = "data/complaints.db"


def create_table():
    """Create complaints table if it does not exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            location TEXT NOT NULL,
            address TEXT NOT NULL,
            severity TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_complaint(description, category, location, address, severity):
    """Insert a new complaint into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO complaints
        (description, category, location, address, severity, date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        description,
        category,
        location,
        address,
        severity,
        datetime.now().strftime("%Y-%m-%d")
    ))


    conn.commit()
    conn.close()



def get_all_complaints():
    """Fetch all complaints from database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM complaints")

    complaints = cursor.fetchall()

    conn.close()

    return complaints
 


def get_total_complaints():
    """Get the total number of complaints in the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM complaints")

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_total_locations():
    """Get the total number of unique locations with complaints."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(DISTINCT location) FROM complaints")

    total = cursor.fetchone()[0]

    conn.close()

    return total