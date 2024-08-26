import sqlite3

def add_stock(symbol, name, price):
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()
    
    c.execute('''
        INSERT INTO stocks (symbol, name, price) VALUES (?, ?, ?)
    ''', (symbol, name, price))
    
    conn.commit()
    conn.close()

def add_dividend(symbol, dividend_amount, dividend_date):
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()
    
    c.execute('''
        SELECT id FROM stocks WHERE symbol = ?
    ''', (symbol,))
    
    stock_id = c.fetchone()
    if stock_id:
        stock_id = stock_id[0]
        c.execute('''
            INSERT INTO dividends (stock_id, dividend_amount, dividend_date) VALUES (?, ?, ?)
        ''', (stock_id, dividend_amount, dividend_date))
        conn.commit()
    
    conn.close()
