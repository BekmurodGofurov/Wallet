import sqlite3 as sq

db = sq.connect('data.db')
cur = db.cursor()

async def db_start():
    cur.execute("""CREATE TABLE IF NOT EXISTS users_data(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                username TEXT,
                age TEXT,
                auth TEXT,
                added_at DATETIME DEFAULT CURRENT_TIMESTAMP)""")

    cur.execute("""CREATE TABLE IF NOT EXISTS wallet_data(
                user_id INTEGER,
                name TEXT,
                price INTEGER,
                added_at DATETIME DEFAULT CURRENT_TIMESTAMP)""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS weekly(
                user_id INTEGER,
                day TEXT,
                total_price INTEGER,
                added_at DATETIME DEFAULT CURRENT_TIMESTAMP)""")

    # cur.execute("""CREATE TABLE IF NOT EXISTS monthly(
    #             user_id INTEGER,
    #             name TEXT,
    #             price INTEGER,
    #             added_at DATETIME DEFAULT CURRENT_TIMESTAMP)""")

# user data
def new_user(user_id, name, username, age, auth):
    cur.execute("SELECT user_id FROM users_data WHERE user_id = ?", (user_id,))
    if cur.fetchone() is None:
        cur.execute("INSERT INTO users_data (user_id, name, username, age, auth) VALUES (?, ?, ?, ?, ?)", (user_id, name, username, age, auth))
        db.commit()
        return True
    else:
        return False

def get_user(user_id):
    cur.execute("SELECT * FROM users_data WHERE user_id = ?", (user_id,))
    row = cur.fetchone()
    if row:
        return row
    else:
        return None

def add_data_wallet(user_id, name, price):
    # Har safar yangi yozuv qo'shish uchun cheklov olib tashlandi
    cur.execute("INSERT INTO wallet_data (user_id, name, price) VALUES (?, ?, ?)", (user_id, name, price))
    db.commit()
    return True

def get_wallet_data(user_id):
    cur.execute("SELECT * FROM wallet_data WHERE user_id = ?", (user_id,))  # Bu yerda user_id ni tuplega o'ralgan
    rows = cur.fetchall()
    if rows:
        return rows
    else:
        return None

def add_weekly_data(user_id, day):
    total_price = 0
    user = get_wallet_data(user_id)
    for i in user:
        total_price += i[2]
    print(total_price)    

    cur.execute("INSERT INTO weekly (user_id, day, total_price) VALUES (?, ?, ?)", (user_id, day, total_price))
# add_weekly_data(5841656536)    