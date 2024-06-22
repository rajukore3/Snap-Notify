from flask import Flask, render_template, request
from app1 import get_prediction_string
import subprocess
import json


app = Flask(__name__)

latitude, longitude = None, None

@app.route('/')
def index():
    return render_template('index.html', prediction=None)

@app.route('/coordinates', methods=['POST'])
def receive_coordinates():
    global latitude, longitude
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    # Process the received coordinates as needed
    print(f'Received coordinates: Latitude={latitude}, Longitude={longitude}')
    return 'Coordinates received successfully'

@app.route('/upload', methods=['POST'])
def upload():
    
    # Get the uploaded file from the form
    uploaded_file = request.files['image']

    # Save the file to a temporary location (you might want to handle this differently)
    uploaded_file.save('uploaded_image.jpg')

    # Call the function from model.py to get the prediction string
    prediction_string = get_prediction_string('uploaded_image.jpg')

    if(prediction_string == "Pothole"):
        javascript_file = "C:\\Users\\korer\\Desktop\\new_proj\\index.js"
        print(prediction_string)
        obj = {"Latitude":latitude, "Longitude":longitude}
        # prediction_string == 'Pothole'
        subprocess.run(["node", javascript_file, json.dumps(obj)])

    # Render the template with the prediction string
    return render_template('index.html', prediction=prediction_string)

@app.route('/result')
def result():
    # Get the prediction string from the query parameters
    prediction_string = request.args.get('prediction')
    javascript_file = "C:\\Users\\korer\\Desktop\\new_proj\\index.js"
    print("Hello", prediction_string)
    # prediction_string == 'Pothole'
    subprocess.run(["node", javascript_file])

    # Render the template with the prediction string
    return render_template('index.html', prediction=prediction_string)

if __name__ == '__main__':
    app.run(debug=True)
