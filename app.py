import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, url_for, flash, redirect
import joblib
import json
import folium

app = Flask(__name__)

# models for predicting house or apartment price with city name

model_house = joblib.load('xgb_rs_model_house_20.11.2020.pkl')
model_apartment = joblib.load('xgb_rs_model_apartment_20.11.2020.pkl')

# models for predicting house or apartment price with postal code

model_house_postal_code = joblib.load('ridge_model_house_25.11.2020.pkl')
model_apartment_postal_code = joblib.load('gbr_rs_model_apartment_21.11.2020.pkl')

# route to home
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

# route direct to predict house price by city name
@app.route("/house",methods=['GET','POST'])
def house():
    return render_template("predict_house.html")

# route direct to predict apartment price by city name
@app.route("/apartment",methods=['GET','POST'])
def apartment():
    return render_template("predict_apartment.html")

# route to direct predict house price by postal code
@app.route("/house_postal_code")
def house_postal_code():
    return render_template("predict_house_postal_code.html")

# route to direct predict apartment price by postal code
@app.route("/apartment_postal_code", methods = ['GET'])
def apartment_postal_code():
    return render_template("predict_apartment_postal_code.html")

# return result of the prediction
@app.route("/result")
def result():
    return render_template("result.html")


# API route (House) for web dev, return json file with the following output:
# 1. predicted price  
# 2. predicted price_sqm
# 3. "city" average price_sqm"  
# 4. difference(%) between predicted price_sqm and average price_sqm

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
    number_of_facades = house['number_of_facades']   
    swimming_pool = house['swimming_pool']  
    state_of_the_building = house['state_of_the_building']   
    construction_year = house['construction_year'] 
    surface_of_the_land = house['surface_of_the_land']

    columns = [x for x in house.keys()]
    int_features = [x for x in house.values()]
    int_features = np.array(int_features) 
    int_features = int_features.reshape(-1,12)
    final_features = pd.DataFrame(int_features,columns=columns)

    prediction = model_house_postal_code.predict(final_features)

    output = round(prediction[0])

    pricem2 = round(output/int(final_features['house_area'][0]))
     
    # to get average house price at postal code given

    postal_code = final_features['postal_code']
    postal_code = int(postal_code)

    df = pd.read_csv('house_price_sqm.csv')
    df['postal_code'] = df['postal_code'].astype('int')

    index = []

    for i in range(df.shape[0]):

        if df['postal_code'][i] == postal_code :
            index.append(i)
            break
        continue
    
    price_sqm = round(df.iloc[index]['price_sqm'].values[0])
    city_name = df.iloc[index]['city_name'].values[0]

    difference = pricem2 - price_sqm

    difference_pct = round(difference/price_sqm* 100,1)

    return {"1. predicted price" : str(output),
            "2. predicted price_sqm" : str(pricem2),
            f"3. {city_name} average price_sqm" : str(price_sqm),
            "4. difference(%)" : str(difference_pct)
            }


# API route (Apartment) for web dev, return json file with the following output:
# 1. predicted price  
# 2. predicted price_sqm
# 3. "city" average price_sqm"  
# 4. difference(%) between predicted price_sqm and average price_sqm

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

    pricem2 = round(output/int(final_features['house_area'][0]))

    # to get average apartment price at postal code given

    postal_code = final_features['postal_code']
    postal_code = int(postal_code)

    df = pd.read_csv('apartment_price_sqm.csv')
    df['postal_code'] = df['postal_code'].astype('int')

    index = []

    for i in range(df.shape[0]):

        if df['postal_code'][i] == postal_code :
            index.append(i)
            break
        continue
    
    price_sqm = round(df.iloc[index]['price_sqm'].values[0])
    city_name = df.iloc[index]['city_name'].values[0]

    difference = pricem2 - price_sqm

    difference_pct = round(difference/price_sqm* 100,1)

    return {"1. predicted price" : str(output),
            "2. predicted price_sqm" : str(pricem2),
            f"3. {city_name} average price_sqm" : str(price_sqm),
            "4. difference(%)" : str(difference_pct)
            }

# route to predict house by city_name
# return 3 prediction text and direct to result.html

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
    
    pricem2 = round(output/int(final_features['house_area'][0]))


    # to get average house price with city name given

    city_name = final_features['city_name']


    df = pd.read_csv('house_price_sqm.csv')
    df['postal_code'] = df['postal_code'].astype('int')

    index = []

    for i in range(df.shape[0]):

        if df['city_name'][i] == city_name[0] :
            index.append(i)
            break
        continue
    
    price_sqm = round(df.iloc[index]['price_sqm'].values[0])
    city_name = df.iloc[index]['city_name'].values[0]

    difference = pricem2 - price_sqm

    return render_template('result.html', 
                            prediction_text1='Predicted house price is € {}  (€ {} /m2)'.format(output,pricem2),
                            text2='Average Price in {} : € {} /m2'.format(city_name,price_sqm),
                            text3='Difference between predicted price/m2 and average price/m2 is {} %'.format(round(difference/price_sqm* 100,1)))

    
# route to predict apartment by city_name
# return 3 prediction text and direct to result.html

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

    pricem2 = round(output/int(final_features['house_area'][0]))

    # to get average house price with city name given

    city_name = final_features['city_name']


    df = pd.read_csv('apartment_price_sqm.csv')
    df['postal_code'] = df['postal_code'].astype('int')

    index = []

    for i in range(df.shape[0]):

        if df['city_name'][i] == city_name[0] :
            index.append(i)
            break
        continue
    
    price_sqm = round(df.iloc[index]['price_sqm'].values[0])
    city_name = df.iloc[index]['city_name'].values[0]

    difference = pricem2 - price_sqm

    return render_template('result.html', 
                            prediction_text1='Predicted apartment price is € {}  (€ {} /m2)'.format(output,pricem2),
                            text2='Average Price in {} : € {} /m2'.format(city_name,price_sqm),
                            text3='Difference between predicted price/m2 and average price/m2 is {} %'.format(round(difference/price_sqm* 100,1)))


# route to predict house by postal code
# return 3 prediction text and direct to result.html

@app.route('/predict_house_postal_code',methods=['GET','POST'])
def predict_house_postal_code():
    '''
    For rendering results on HTML GUI
    '''
    columns = ['postal_code', 'number_of_rooms', 'house_area', 'fully_equipped_kitchen',
    'open_fire', 'terrace', 'garden','number_of_facades', 'swimming_pool', 
    'state_of_the_building','construction_year','surface_of_the_land']

    int_features = [x for x in request.form.values()]
    int_features = np.array(int_features) 
    int_features = int_features.reshape(-1,12)
    final_features = pd.DataFrame(int_features,columns=columns)

    prediction = model_house_postal_code.predict(final_features)

    output = round(prediction[0])

    pricem2 = round(output/int(final_features['house_area'][0]))


    # to get average house price at postal code given

    postal_code = final_features['postal_code']
    postal_code = int(postal_code)

    df = pd.read_csv('house_price_sqm.csv')
    df['postal_code'] = df['postal_code'].astype('int')

    index = []

    for i in range(df.shape[0]):

        if df['postal_code'][i] == postal_code :
            index.append(i)
            break
        continue
    
    price_sqm = round(df.iloc[index]['price_sqm'].values[0])
    city_name = df.iloc[index]['city_name'].values[0]

    difference = pricem2 - price_sqm

    return render_template('result.html', 
                            prediction_text1='Predicted house price is € {}  (€ {} /m2)'.format(output,pricem2),
                            text2='Average Price for {} : € {} /m2'.format(city_name,price_sqm),
                            text3='Different between predicted price/m2 and average price/m2 is {} %'.format(round(difference/price_sqm* 100,1)))


# route to predict apartment by postal code
# return 3 prediction text and direct to result.html

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

    # to get average apartment price at postal code given

    postal_code = final_features['postal_code']
    postal_code = int(postal_code)

    df = pd.read_csv('apartment_price_sqm.csv')
    df['postal_code'] = df['postal_code'].astype('int')

    index = []

    for i in range(df.shape[0]):

        if df['postal_code'][i] == postal_code :
            index.append(i)
            break
        continue
    
    price_sqm = round(df.iloc[index]['price_sqm'].values[0])
    city_name = df.iloc[index]['city_name'].values[0]

    difference = pricem2 - price_sqm

    return render_template('result.html', 
                            prediction_text1='Predicted apartment price is € {}  (€ {} /m2)'.format(output,pricem2),
                            text2='Average Price for {} : € {} /m2'.format(city_name,price_sqm),
                            text3='Different between predicted price/m2 and average price/m2 is {} %'.format(round(difference/price_sqm* 100,1)))
     
# route to render average_house_price

@app.route('/average_house_price', methods=['GET','POST'])
def average_house_price():
    # given a postal code to render average house price
    postal_code = 1000
    
    #house = request.get_json(force=True)
    #postal_code = house['postal_code'] 

    #postal_code = [x for x in house.values()]
    #postal_code = house.postal_code

    columns = [x for x in house.keys()]
    postal_code = [x for x in house.values()]
     

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

# route to render average_apartment_price

@app.route('/average_apartment_price', methods=['GET','POST'])
def average_apartment_price():
    # given a postal code to render average apartment price
    postal_code = 1000

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

# route to render average houseprice for cities
@app.route('/map_average_house_price', methods=['GET','POST'])
def map_average_house_price():
    return render_template("average_price_per_sqm_belgium_house.html")

# route to render average apartmentprice for cities
@app.route('/map_average_apartment_price', methods=['GET','POST'])
def map_average_apartment_price():
    return render_template("average_price_per_sqm_belgium_apartment.html")
 
if __name__ == "__main__":
    app.run(debug=True)