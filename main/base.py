import sqlite3

conn = sqlite3.connect("server.db")
cur = conn.cursor()
#Создаю базу данных с профилем пользователя
cur.execute("""CREATE TABLE IF NOT EXISTS user(
            name TEXT,
            money INTEGER);
            """)
conn.commit()
#Создаю базу данных с профилем пользователя
cur.execute("""CREATE TABLE IF NOT EXISTS achievement(
            id INTEGER,
            task TEXT,
            ismade INTEGER);
            """)
conn.commit()
