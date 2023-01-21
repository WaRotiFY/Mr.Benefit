import sqlite3

conn = sqlite3.connect("server.db")
cur = conn.cursor()
#Создаю базу данных с профилем пользователя
cur.execute("""CREATE TABLE IF NOT EXISTS user(
            TEXT name,
            INTEGER money);
            """)
conn.commit()
#Создаю базу данных с профилем пользователя
cur.execute("""CREATE TABLE IF NOT EXISTS achievement(
            TEXT task,
            INTEGER ismade);
            """)
conn.commit()
