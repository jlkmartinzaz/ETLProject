import sqlite3
from config.config import Config

conn = sqlite3.connect(Config.SQLITE_DB_PATH)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS nvidia_data (
    Date TEXT,
    Open REAL,
    High REAL,
    Low REAL,
    Close REAL,
    Adj_Close REAL,
    Volume INTEGER
)
''')

conn.commit()
conn.close()
print("Tabla nvidia_data lista con las columnas correctas.")

