from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "MT5 Flask API is running on VPS"

@app.route('/login', methods=['POST'])
def save_login():
    try:
        data = request.json
        with open('login_credentials.json', 'w') as f:
            json.dump(data, f)
        return jsonify({'message': 'Login credentials saved'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/trade', methods=['POST'])
def save_trade():
    data = request.get_json()
    try:
        with open("trade_instructions.json", "w") as f:
            json.dump(data, f)
        return jsonify({"message": "Trade instructions saved."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/toggle-ea', methods=['POST'])
def toggle_ea():
    data = request.get_json()
    try:
        status = "on" if data.get("enabled") else "off"
        with open("ea_status.txt", "w") as f:
            f.write(status)
        return jsonify({"message": f"EA status set to {status}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/status', methods=['GET'])
def get_status():
    try:
        if os.path.exists("ea_status.txt"):
            with open("ea_status.txt", "r") as f:
                status = f.read().strip()
                return jsonify({"ea_enabled": status == "on"})
        return jsonify({"ea_enabled": False})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/account', methods=['GET'])
def get_account_stub():
    return jsonify({
        "login": 123456,
        "name": "Demo Account",
        "leverage": 100,
        "balance": 10000.0,
        "equity": 9800.0,
        "free_margin": 9500.0
    })

@app.route('/positions', methods=['GET'])
def get_positions_stub():
    return jsonify([])

@app.route('/orders', methods=['GET'])
def get_orders_stub():
    return jsonify([])

@app.route('/symbols', methods=['GET'])
def get_symbols_stub():
    return jsonify(["EURUSD", "XAUUSD", "GBPUSD"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
