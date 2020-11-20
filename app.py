import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, url_for, flash, redirect
import joblib
import json

app = Flask(__name__)
model_house = joblib.load('xgb_rs_model_house_20.11.2020.pkl')
model_apartment = joblib.load('xgb_rs_model_apartment_20.11.2020.pkl')

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/house")
def house():
    return render_template("predict_house.html")

@app.route("/apartment", methods = ['GET'])
def apartment():
    return render_template("predict_apartment.html")
 
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
    #render_template('result.html', prediction_text='Predicted price for the house is € {}'.format(output))

 
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

    final_features['prediction'] = output

    result = final_features.to_json(index=False,orient="split")
    parsed = json.loads(result)
    
    return json.dumps(parsed, indent=4)
    

    #return final_features.json(),render_template('result.html', prediction_text='Predicted price for the apartment is € {}'.format(output))

 

if __name__ == "__main__":
    app.run(debug=True)