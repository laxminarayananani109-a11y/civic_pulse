"""Import complaints from CSV into SQLite database."""
import sqlite3
import pandas as pd

# Read CSV
df = pd.read_csv("data/complaints.csv")

# Connect DB
conn = sqlite3.connect("data/complaints.db")

# Replace old table with new data
df.to_sql("complaints", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("Imported", len(df), "complaints successfully!")
