import sqlite3

DATABASE = 'incidents.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS incidents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                incident_type TEXT NOT NULL,
                description TEXT NOT NULL,
                date TEXT NOT NULL,
                status TEXT NOT NULL
            )
        ''')
        conn.commit()

def add_incident(incident_type, description, date, status):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO incidents (incident_type, description, date, status)
            VALUES (?, ?, ?, ?)
        ''', (incident_type, description, date, status))
        conn.commit()

def get_incidents():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM incidents')
        return cursor.fetchall()
