# Pace-Calculator-Microservice

This program is a simple microservice to calculate pace data. 

### Requirements:
1. Python 3.9 or later installed
2. Flask module installed
3. A way to make HTTP requests
    - Can be done via the "requests" module if your app is in python
    - Run "pip install requests" in terminal


### Starting the Microservice:
1. Download Pace_Micro.py from this repo
2. Adjust the "host" and "port" variables in line 33 as desired, or leave default
3. Run the file, and check the terminal to confirm the server has launched successfully.

### Making a request/Accepting a response:
1. First, you must package the request data into a json of format {"distance": A, duration: B"} where A and B are floats or integers.
2. You must make a HTML POST request to the following domain "http://localhost:5001/calculate_pace" (or whatever you set as the domain & port).
3. When you receive the response, you must extract out the json data, and from that
the calculated pace data.
4. Below is an example of how you can do this using the "Flask" and "requests" python modules
```
from flask import Flask, request, render_template_string
import requests


data = {"distance": 5.5, "duration": 10}

response = requests.post("http://localhost:5001/calculate_pace", json=data)

pace_data = response.json()

pace = round(pace_data.get("pace"), 2)  # Extracts the pace value from the reponse
```

### UML Diagram
![Alt](UML.png)
