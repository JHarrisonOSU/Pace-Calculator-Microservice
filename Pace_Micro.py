"""
This pace calculator microservice runs locally on the chosen port (default = 5001), and has 
an endpoint for POST requests at "/calculate_pace" where another local server may submit 
a request with the input data, and received a response containing the calculated pace.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)


# Create our endpoint
@app.route("/calculate_pace", methods=["POST"])
def calculate_pace():
    # Extract and process data
    data = request.get_json()
    distance = float(data.get("distance", 0))
    duration = float(data.get("duration", 0))
    pace = duration / distance if distance else 0

    # Print to console for debugging
    print(
        f" \n Service Called: \n Distance: {distance} \n Duration: {duration} \n Calculated Pace: {pace} \n"
    )

    # Return pace data in json via response
    return jsonify({"pace": pace}), 200


# App runs on localhost, port 5001 (Modify this if necessary)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
