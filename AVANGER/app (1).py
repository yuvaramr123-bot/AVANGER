from flask import Flask, jsonify
from services.fish_prediction import predict_fish_location
from services.weather_service import get_weather_alert
from services.market_forecast import get_market_forecast
from models.route_optimizer import optimize_route

app = Flask(__name__)

@app.route("/fish-location")
def fish_location():
    result = predict_fish_location()
    return jsonify(result)

@app.route("/weather-alert")
def weather_alert():
    result = get_weather_alert()
    return jsonify(result)

@app.route("/market-price")
def market_price():
    result = get_market_forecast()
    return jsonify(result)

@app.route("/optimized-route")
def optimized_route():
    result = optimize_route()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)