from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculate_pace", methods=["POST"])
def calculate_pace():
    data = request.get_json()
    distance = float(data.get("distance", 0))
    duration = float(data.get("duration", 0))
    pace = duration / distance if distance else 0
    print(
        f"\nService Called: \n Distance: {distance} \n Duration: {duration} \n Calculated Pace: {pace} \n"
    )
    return jsonify({"pace": pace}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
