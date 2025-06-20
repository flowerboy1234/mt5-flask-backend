from flask import Flask, request, jsonify
import MetaTrader5 as mt5
import json

app = Flask(__name__)

# Connect to MT5
mt5.initialize()

@app.route('/')
def home():
    return "MT5 Flask API is running"

@app.route('/account')
def account():
    acc = mt5.account_info()
    return jsonify({
        "login": acc.login,
        "name": acc.name,
        "leverage": acc.leverage,
        "balance": acc.balance,
        "equity": acc.equity,
        "free_margin": acc.margin_free
    })

@app.route('/positions')
def positions():
    positions = mt5.positions_get()
    return jsonify([{
        "ticket": p.ticket,
        "symbol": p.symbol,
        "volume": p.volume,
        "price_open": p.price_open,
        "sl": p.sl,
        "tp": p.tp,
        "profit": p.profit
    } for p in positions]) if positions else jsonify([])

@app.route('/orders')
def orders():
    orders = mt5.orders_get()
    return jsonify([{
        "ticket": o.ticket,
        "symbol": o.symbol,
        "type": o.type,
        "volume": o.volume_current,
        "price": o.price_open,
        "sl": o.sl,
        "tp": o.tp,
        "comment": o.comment
    } for o in orders]) if orders else jsonify([])

@app.route('/symbols')
def symbols():
    visible = mt5.symbols_get()
    return jsonify([s.name for s in visible]) if visible else jsonify([])

@app.route('/trade', methods=['POST'])
def trade():
    data = request.json
    with open("trade_instructions.json", "w") as f:
        json.dump(data, f)
    return jsonify({"status": "saved"})

@app.route('/toggle-ea', methods=['POST'])
def toggle_ea():
    status = request.json.get("enabled")
    with open("ea_status.txt", "w") as f:
        f.write("1" if status else "0")
    return jsonify({"ea_enabled": status})

@app.route('/status')
def status():
    try:
        with open("ea_status.txt", "r") as f:
            flag = f.read().strip()
        return jsonify({"ea_enabled": flag == "1"})
    except:
        return jsonify({"ea_enabled": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
