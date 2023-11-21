'''
This is a simple demo server that calls the pace microservice after a user submits data to a form.
'''

from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# HTML template for the form
FORM_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Pace Calculator</title>
</head>
<body>
    <h2>Pace Calculator</h2>
    <form method="post" action="/submit_data">
        Distance (in kilometers): <input type="text" name="distance"><br>
        Duration (in minutes): <input type="text" name="duration"><br>
        <input type="submit" value="Calculate Pace">
    </form>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(FORM_TEMPLATE)


@app.route("/submit_data", methods=["POST"])
def submit_data():
    distance = request.form.get("distance")
    duration = request.form.get("duration")

    # Prepare the data for the POST request
    data = {"distance": distance, "duration": duration}

    # Make a POST request to the microservice server
    response = requests.post("http://localhost:5001/calculate_pace", json=data)

    pace_data = response.json()
    print(f"\nGot response. \n Data: {pace_data} \n")
    pace = round(pace_data.get("pace"), 2)

    return f"Your pace is {pace} minutes per kilometer"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
