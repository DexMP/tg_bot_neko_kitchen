import sqlite3 as sq

db = sq.connect('database.db')
cur = db.cursor

async def db_start():
    cur.execute("CREATE TABLE IF NOT EXIST accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "role TEXT, "
                "cart_id TEXT, "
                "phone TEXT,"
                "coins INTEGER)")
    db.commit()
    db.close()