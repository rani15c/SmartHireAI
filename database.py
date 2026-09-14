import sqlite3

DATABASE = "smartHire.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            qualification TEXT NOT NULL,
            experience INTEGER NOT NULL,
            specialization TEXT NOT NULL,
            score INTEGER NOT NULL,
            status TEXT NOT NULL,
            interview_score INTEGER DEFAULT 0,
            interview_status TEXT DEFAULT 'Not Completed',
            selection_status TEXT DEFAULT 'Under Review'
        )
    """)

    # Keep existing local databases compatible with the current dashboard.
    candidate_columns = {
        column[1]
        for column in connection.execute("PRAGMA table_info(candidates)")
    }
    if "selection_status" not in candidate_columns:
        connection.execute("""
            ALTER TABLE candidates
            ADD COLUMN selection_status TEXT DEFAULT 'Under Review'
        """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Create default admin account
    existing_admin = connection.execute(
        "SELECT * FROM admins WHERE username = ?",
        ("admin",)
    ).fetchone()

    if existing_admin is None:
        connection.execute(
            "INSERT INTO admins (username, password) VALUES (?, ?)",
            ("admin", "admin123")
        )

    connection.commit()
    connection.close()