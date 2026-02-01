import sqlite3
from src.data.database import Database

db = Database()
conn = db.conn
cursor = conn.cursor()

# Add notes column if missing
cursor.execute("PRAGMA table_info(sessions)")
columns = [col[1] for col in cursor.fetchall()]
if 'notes' not in columns:
    cursor.execute("ALTER TABLE sessions ADD COLUMN notes TEXT DEFAULT ''")
    conn.commit()
    print("✅ Added 'notes' column to sessions table")

conn.close()
