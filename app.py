import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, url_for, flash, redirect
import joblib
import json
import folium

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

@app.route("/predict_house_tojson", methods=['GET','POST'])
def predict_house_tojson():

    house = {'postal_code': '3271',
            'number_of_rooms': 4,
            'house_area' : 226,
            'fully_equipped_kitchen': 'yes',
            'open_fire':'no',
            'terrace': 'yes',
            'garden': 'yes',
            'surface_of_the_land' : 398,
            'number_of_facades': 3,
            'swimming_pool': 'no',
            'state_of_the_building': 'to renovate',
            'construction_year' : 1930}

    columns = [x for x in house.keys()]
    int_features = [x for x in house.values()]
    int_features = np.array(int_features) 
    int_features = int_features.reshape(-1,12)
    final_features = pd.DataFrame(int_features,columns=columns)

    prediction = model_house_postal_code.predict(final_features)

    output = round(prediction[0])
    
    final_features['Predicted Price'] = output

    result = final_features.to_json(index=False,orient="split")
    parsed = json.loads(result)
    
    return  json.dumps(parsed, indent=4) 

@app.route("/predict_house_tojson2", methods=['GET','POST'])
def predict_house_tojson2():

    house = request.get_json(force=True)
    postal_code = house['postal_code'] 
    number_of_rooms = house['number_of_rooms']  
    house_area = house['house_area']  
    fully_equipped_kitchen = house['fully_equipped_kitchen'] 
    open_fire = house['open_fire']  
    terrace = house['terrace']  
    garden = house['garden']   
    surface_of_the_land = house['surface_of_the_land']   
    number_of_facades = house['number_of_facades']   
    swimming_pool = house['swimming_pool']  
    state_of_the_building = house['state_of_the_building']   
    construction_year = house['construction_year'] 

    columns = [x for x in house.keys()]
    int_features = [x for x in house.values()]
    int_features = np.array(int_features) 
    int_features = int_features.reshape(-1,12)
    final_features = pd.DataFrame(int_features,columns=columns)

    prediction = model_house_postal_code.predict(final_features)

    output = round(prediction[0])
     
    return str(output) 

@app.route("/predict_apartment_tojson2", methods=['GET','POST'])
def predict_apartment_tojson2():

    house = request.get_json(force=True)
    postal_code = house['postal_code'] 
    number_of_rooms = house['number_of_rooms']  
    house_area = house['house_area']  
    fully_equipped_kitchen = house['fully_equipped_kitchen'] 
    open_fire = house['open_fire']  
    terrace = house['terrace']  
    garden = house['garden']   
    number_of_facades = house['number_of_facades']   
    swimming_pool = house['swimming_pool']  
    state_of_the_building = house['state_of_the_building']   
    construction_year = house['construction_year'] 

    columns = [x for x in house.keys()]
    int_features = [x for x in house.values()]
    int_features = np.array(int_features) 
    int_features = int_features.reshape(-1,11)
    final_features = pd.DataFrame(int_features,columns=columns)

    prediction = model_apartment_postal_code.predict(final_features)

    output = round(prediction[0])
     
    return str(output) 

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


@app.route('/average_house_price', methods=['GET','POST'])
def average_house_price():

    postal_code = 1000
    #house = request.get_json(force=True)
    #postal_code = house['postal_code'] 

    #postal_code = [x for x in house.values()]
    #postal_code = house.postal_code

    df = pd.read_csv('house_price_sqm.csv')
    df['postal_code'] = df['postal_code'].astype('int')

    index = []

    for i in range(df.shape[0]):

        if df['postal_code'][i] == postal_code :
            index.append(i)
            break
        continue
    long,lat = df['longitude'][index][index[0]] ,df['lattitude'][index][index[0]] 

    m = folium.Map(location=[lat,long] ,zoom_start=15)

    folium.Marker(
            location = [lat,long],
            tooltip =   '<li><bold>Property : ' 'House'+
                        '<li><bold>Region : '+str(df.loc[index]['region'].tolist()[0])+
                        '<li><bold>Province : '+str(df.loc[index]['province'].tolist()[0])+
                        '<li><bold>City Name : '+str(df.loc[index]['city_name'].tolist()[0])+
                        '<li><bold>Postal Code : '+str(df.loc[index]['postal_code'].tolist()[0])+
                        '<li><bold>Average Price_sqm : '+str(round(df.loc[index]['price_sqm'].tolist()[0])),
            popup = [lat,long]).add_to(m)


    return m._repr_html_()

@app.route('/average_apartment_price', methods=['GET','POST'])
def average_apartment_price():

    postal_code = 1000
    #house = request.get_json(force=True)
    #postal_code = house['postal_code'] 

    #postal_code = [x for x in house.values()]
    #postal_code = house.postal_code

    df = pd.read_csv('apartment_price_sqm.csv')
    df['postal_code'] = df['postal_code'].astype('int')

    index = []

    for i in range(df.shape[0]):

        if df['postal_code'][i] == postal_code :
            index.append(i)
            break
        continue
    long,lat = df['longitude'][index][index[0]] ,df['lattitude'][index][index[0]] 

    m = folium.Map(location=[lat,long] ,zoom_start=15)

    folium.Marker(
            location = [lat,long],
            tooltip =   '<li><bold>Property : ' 'House'+
                        '<li><bold>Region : '+str(df.loc[index]['region'].tolist()[0])+
                        '<li><bold>Province : '+str(df.loc[index]['province'].tolist()[0])+
                        '<li><bold>City Name : '+str(df.loc[index]['city_name'].tolist()[0])+
                        '<li><bold>Postal Code : '+str(df.loc[index]['postal_code'].tolist()[0])+
                        '<li><bold>Average Price_sqm : '+str(round(df.loc[index]['price_sqm'].tolist()[0])),
            popup = [lat,long]).add_to(m)


    return m._repr_html_()

@app.route('/map_average_house_price', methods=['GET','POST'])
def map_average_house_price():
    return render_template("average_price_per_sqm_belgium_house.html")


@app.route('/map_average_apartment_price', methods=['GET','POST'])
def map_average_apartment_price():
    return render_template("average_price_per_sqm_belgium_apartment.html")
 



if __name__ == "__main__":
    app.run(debug=True)