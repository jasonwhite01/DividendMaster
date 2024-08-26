import sqlite3

def initialize_database():
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS stocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT UNIQUE NOT NULL,
            name TEXT,
            price REAL
        )
    ''')
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS dividends (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stock_id INTEGER,
            dividend_amount REAL,
            dividend_date TEXT,
            FOREIGN KEY (stock_id) REFERENCES stocks (id)
        )
    ''')
    
    conn.commit()
    conn.close()

initialize_database()
