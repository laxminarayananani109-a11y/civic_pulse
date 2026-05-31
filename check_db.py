import sqlite3

conn = sqlite3.connect("data/complaints.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM complaints")
rows = cursor.fetchall()

print(f"Total Complaints: {len(rows)}")

for row in rows:
    print(row)

conn.close()
