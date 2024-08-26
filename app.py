from flask import Flask, request, jsonify
from src.com.dividend import calculate_dividend_yield
from src.com.stock import add_dividend, add_stock

app = Flask(__name__)

@app.route('/add_stock', methods=['POST'])
def api_add_stock():
    data = request.json
    add_stock(data['symbol'], data['name'], data['price'])
    return jsonify({'status': 'success'}), 201

@app.route('/add_dividend', methods=['POST'])
def api_add_dividend():
    data = request.json
    add_dividend(data['symbol'], data['dividend_amount'], data['dividend_date'])
    return jsonify({'status': 'success'}), 201

@app.route('/dividend_yield/<symbol>', methods=['GET'])
def api_dividend_yield(symbol):
    yield_percent = calculate_dividend_yield(symbol)
    if yield_percent is not None:
        return jsonify({'dividend_yield': yield_percent})
    else:
        return jsonify({'error': 'Stock not found or invalid data'}), 404
    
# TODO: add route for calculating annual return of dividends for a single unit of a given symbols' stock

if __name__ == '__main__':
    app.run(debug=True)
