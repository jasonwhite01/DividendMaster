import sqlite3

def calculate_dividend_yield(symbol):
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()
    
    # Fetch stock price
    c.execute('''
        SELECT price FROM stocks WHERE symbol = ?
    ''', (symbol,))
    
    stock_price = c.fetchone()
    if stock_price:
        stock_price = stock_price[0]
        
        # Fetch total annual dividends
        c.execute('''
            SELECT SUM(dividend_amount) FROM dividends
            JOIN stocks ON stocks.id = dividends.stock_id
            WHERE stocks.symbol = ?
        ''', (symbol,))
        
        total_dividends = c.fetchone()
        if total_dividends:
            total_dividends = total_dividends[0]
            if stock_price > 0:
                dividend_yield = (total_dividends / stock_price) * 100
                return dividend_yield
            else:
                return None
    
    conn.close()
    return None

def calculate_annual_dividend_return_per_share(symbol):

    # TODO: Add implementation
    return None
