import json
from flask import Flask, jsonify

app = Flask(__name__)

# Load data
def load_airports_data():
    with open('airports.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# API
@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    airports = load_airports_data()

    airport = airports.get(icao.upper())

    if airport:
        return jsonify({
            "icao": airport["icao"],
            "name": airport["name"],
            "city": airport["city"],
            "country": airport["country"]
        })

    return jsonify({"message": "Airport not found"}), 404

# Run server
if __name__ == '__main__':
    app.run(debug=True, port=5000)