"""Database utilities for Civic Pulse complaint management."""
import sqlite3
from datetime import datetime

DB_PATH = "data/complaints.db"


def create_table():
    """Create the complaints table if it does not exist."""
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


def add_complaint(description, category, location):
    """Add a new complaint to the database."""
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
    """Retrieve all complaints from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM complaints")

    complaints = cursor.fetchall()

    conn.close()

    return complaints
 


def get_total_complaints():
    """Get the total count of complaints in the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM complaints")

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_total_locations():
    """Get the total count of unique locations in the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(DISTINCT location) FROM complaints")

    total = cursor.fetchone()[0]

    conn.close()

    return total
