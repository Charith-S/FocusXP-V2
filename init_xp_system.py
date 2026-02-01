from src.data.database import Database

db = Database()
cursor = db.conn.cursor()

# XP table
cursor.execute("""
CREATE TABLE IF NOT EXISTS xp_system (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER,
    xp_earned INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    total_xp INTEGER DEFAULT 0,
    FOREIGN KEY (session_id) REFERENCES sessions (id)
)
""")

# Trigger: Auto-calculate XP on session insert/update
cursor.execute("""
CREATE TRIGGER IF NOT EXISTS calculate_xp
AFTER INSERT ON sessions
FOR EACH ROW
BEGIN
    INSERT INTO xp_system (session_id, xp_earned, total_xp)
    VALUES (NEW.id, (NEW.duration / 60) * 10, (NEW.duration / 60) * 10);
END;
""")

db.conn.commit()
print("✅ XP system initialized!")
