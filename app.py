import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from flask import Flask, render_template, request, jsonify
import pickle

from chat import get_response

app = Flask(__name__, template_folder='/Users/pragatimehra/Desktop/Delhi/templates')
data = pd.read_excel("Cleaned-Delhi-Prices.xlsx")
model = pickle.load(open('model.pkl', 'rb'))
le = LabelEncoder()
x = le.fit_transform(data['Location'])

# Function to get list of property dealers with contact numbers for a given location
def get_property_dealers_with_contacts(location):
    property_dealers = [
        {'name': 'Mohit Tiwari', 'contact': '9876543210'},
        {'name': 'Naman Gaur', 'contact': '8765432190'},
        {'name': 'Pragati Mehra', 'contact': '7654321980'},
        {'name': 'Suyash Tyagi', 'contact': '6543219870'},
        {'name': 'Swaagatam Team', 'contact': '9999999999'}
    ]
    return property_dealers

@app.route('/')
def index():
    locations = sorted(data['Location'].unique())
    return render_template('home.html', locations=locations)

@app.route('/chat', methods=['POST'])
def chat():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    area = request.form.get('area')
    bhk = request.form.get('bhk')
    ne = request.form.get('toggle')
    at = request.form.get('atm')
    se = request.form.get('security')
    ca = request.form.get('car')
    li = request.form.get('lift')
    n = 0
    for i in range(414):
        if data['Location'][i] == location:
            n = i
            break
    if at == 'on':
        atm = 1
    else:
        atm = 0
    if se == 'on':
        security = 1
    else:
        security = 0
    if ca == 'on':
        car = 1
    else:
        car = 0
    if li == 'on':
        lift = 1
    else:
        lift = 0
    if ne == 'on':
        new = 1
    else:
        new = 0
    print(area, x[n], bhk, new, atm, security, car, lift)
    input_data = pd.DataFrame([[area, x[n], bhk, new, atm, security, car, lift]],
                              columns=['Area', 'Location', 'No. of Bedrooms', 'Resale', 'ATM', '24X7Security', 'CarParking', 'LiftAvailable'])
    pred = model.predict(input_data)[0] * 1e6

    # Retrieve list of property dealers with contact numbers for the predicted location
    property_dealers = get_property_dealers_with_contacts(location)

    # return str(np.round(pred, 2))
    
    # Return predicted price and list of property dealers with contact numbers as JSON response
    response = {
        'predicted_price': np.round(pred, 2),
        'property_dealers': property_dealers,
        'location': location
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
