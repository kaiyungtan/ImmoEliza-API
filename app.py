import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, url_for, flash, redirect
import joblib
import json

app = Flask(__name__)
model_house = joblib.load('xgb_rs_model_house_20.11.2020.pkl')
model_apartment = joblib.load('xgb_rs_model_apartment_20.11.2020.pkl')
model_house_postal_code = joblib.load('ridge_model_house_21.11.2020.pkl')
model_apartment_postal_code = joblib.load('gbr_rs_model_apartment_21.11.2020.pkl')

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/house",methods=['GET','POST'])
def house():
    return render_template("predict_house.html")

@app.route("/apartment",methods=['GET','POST'])
def apartment():
    return render_template("predict_apartment.html")

@app.route("/house_postal_code")
def house_postal_code():
    return render_template("predict_house_postal_code.html")

@app.route("/apartment_postal_code", methods = ['GET'])
def apartment_postal_code():
    return render_template("predict_apartment_postal_code.html")

@app.route("/result")
def result():
    return render_template("result.html")

@app.route('/predict_house',methods=['GET','POST'])
def predict_house():
    '''
    For rendering results on HTML GUI
    '''
    columns = ['city_name', 'number_of_rooms', 'house_area', 'fully_equipped_kitchen',
    'open_fire', 'terrace', 'garden', 'surface_of_the_land','number_of_facades', 
    'swimming_pool', 'state_of_the_building','construction_year', 'province', 'region']

    int_features = [x for x in request.form.values()]
    int_features = np.array(int_features) 
    int_features = int_features.reshape(-1,14)
    final_features = pd.DataFrame(int_features,columns=columns)

    prediction = model_house.predict(final_features)

    output = round(prediction[0])
    
    final_features['Predicted Price'] = output

    result = final_features.to_json(index=False,orient="split")
    parsed = json.loads(result)
    
    return json.dumps(parsed, indent=4) 
    

@app.route('/predict_apartment',methods=['GET','POST'])
def predict_apartment():
    '''
    For rendering results on HTML GUI

    '''
    columns = ['city_name', 'number_of_rooms', 'house_area', 'fully_equipped_kitchen',
    'open_fire', 'terrace', 'garden', 'number_of_facades', 'swimming_pool', 
    'state_of_the_building','construction_year', 'province', 'region']

    int_features = [x for x in request.form.values()]
    int_features = np.array(int_features) 
    int_features = int_features.reshape(-1,13)
    final_features = pd.DataFrame(int_features,columns=columns)

    prediction = model_apartment.predict(final_features)

    output = round(prediction[0])

    final_features['Predicted Price'] = output

    result = final_features.to_json(index=False,orient="split")
    parsed = json.loads(result)
    
    return json.dumps(parsed, indent=4)
    

@app.route('/predict_house_postal_code',methods=['GET','POST'])
def predict_house_postal_code():
    '''
    For rendering results on HTML GUI
    '''
    columns = ['postal_code', 'number_of_rooms', 'house_area', 'fully_equipped_kitchen',
    'open_fire', 'terrace', 'garden', 'surface_of_the_land','number_of_facades', 
    'swimming_pool', 'state_of_the_building','construction_year']

    int_features = [x for x in request.form.values()]
    int_features = np.array(int_features) 
    int_features = int_features.reshape(-1,12)
    final_features = pd.DataFrame(int_features,columns=columns)

    prediction = model_house_postal_code.predict(final_features)

    output = round(prediction[0])

    pricem2 = round(output/int(final_features['house_area'][0]))
    
    return render_template('result.html', 
                            prediction_text1='Predicted house price is € {}'.format(output),
                            prediction_text2='Price per Square Meter : € {} /m2'.format(pricem2))

@app.route('/predict_apartment_postal_code',methods=['GET','POST'])
def predict_apartment_postal_code():
    '''
    For rendering results on HTML GUI

    '''
    columns = ['postal_code', 'number_of_rooms', 'house_area', 'fully_equipped_kitchen',
    'open_fire', 'terrace', 'garden', 'number_of_facades','swimming_pool', 
    'state_of_the_building','construction_year']

    int_features = [x for x in request.form.values()]
    int_features = np.array(int_features) 
    int_features = int_features.reshape(-1,11)
    final_features = pd.DataFrame(int_features,columns=columns)

    prediction = model_apartment_postal_code.predict(final_features)

    output = round(prediction[0])

    pricem2 = round(output/int(final_features['house_area'][0]))

    return render_template('result.html', 
                            prediction_text1='Predicted apartment price is € {}'.format(output),
                            prediction_text2='Price per Square Meter : € {} /m2'.format(pricem2))

if __name__ == "__main__":
    app.run(debug=True)