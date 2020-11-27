<img width="1127" alt="Screenshot 2020-11-26 at 19 02 44" src="https://user-images.githubusercontent.com/69633814/100381811-15ebf400-301a-11eb-98b9-22263511e16a.png">

# ImmoEliza-API

To create an API that will make price forecasts on houses or apartments according to certain parameters (postal code, number of rooms, surface area, etc.)

* Website (AI Dev) - https://immoeliza-real-estate.herokuapp.com/

* Github page - https://kaiyungtan.github.io/ImmoEliza-API/

* Website (Web Dev) - 

* Github repo (Web Dev) -

## Background

This project is a collaboration between BeCode AI and the BeCode Web 
Dev team.

The AI developers will create an API and the web developers will develop an interface for the client "ImmoEliza". 

The main process is about a collaboration between the AI and the web dev so that all have to be in sync in order to know how to construct the form.

Team Members consists of: 

* AI Dev  : Adam 

* Web Dev : Valentin, Henrique, Nathanaël 

    
## Mission objectives  

* Be able to create a prediction model
* Be able to deploy model
* Be able to work in a team
* Be able to build an api

## The Mission

You need to create an API that will make price forecasts on houses or apartments according to certain parameters (postal code, number of rooms, surface area, etc...). This API will be used by web devs who will be able to use it to create an interface for the ImmoEliza agency.


## Use Case examples:
 
* to find out what is the predicted price of a house or apartment based on your selection criteria.
* to compare the asking price of what is posted on the real estate website i.e ImmoWeb with what is predicted price.
* to compare the price per square meter of the property with the average price per square meter of the city


### Must-have features

* The api must be functional 
* Your model must be functional


### Additional features

* to provide house/apartment average price (square per meter) for all cities in Belgium
* to show the difference (%) between house/apartment sq/m2 versus the average sq/m2 for the city


## Machine Learning Process Overview

![image](https://user-images.githubusercontent.com/69633814/100385145-1ab4a600-3022-11eb-9674-af2276a16f9e.png)

## Business Understanding 

* Getting a good estimate of the price of a house or apartment is hard even for the most seasoned real estate agents. It involves a lot of variables. The owner of the property can determine the price based on many factors. The property itself is of course the main factor to determine the price. However the location and facilities around the property can hugely impact the price. In addition, the inflation rate or personal reason can also play a part in influencing the price.

* In this project, we are using different machine learning algorithms to learn from the features of the real estate in order to predict the price. The models neither take into account of the facilities around the real estate , nor it include other external factors i.e COVID-19 effect on the housing prices.

* The price prediction is based on the price that posted on the website and not the actual transaction of the property. With this in mind, we can assume that when listing the property , most of the owner will probably put a higher price for room of negoatiation.

* According to [STATBEL](https://statbel.fgov.be/en/themes/housing/house-price-index#news):

	* The observed annual inflation rate for house prices amounts to 4.5 % in the second quarter of 2020 compared to 3.5 % in the previous quarter.

	* The average inflation rate for the last four quarters amounts to 4.3 %.

	* The house price index went up by 1.4 % in the second quarter of 2020 compared to the previous quarter.

	* The house price index can be broken down by new houses and existing houses. In the second quarter of 2020, annual inflation amounted to 5.3 % for new houses and 4.3 % for existing houses. 

note: The house price index measures the price evolution with the assumption that the characteristics of the property sold remain unchanged.


## Data Understanding

* The dataset for the real estate were scrapped form [Immoweb](https://www.immoweb.be/) probably the biggest real estate website in Belgium mid of September 2020 with more than 50,000 of properties including houses and apartments from a previous BeCode [Data Collecting Challenge](https://github.com/kaiyungtan/challenge-collecting-data).

* Initially the dataset have 52077 rows and 20 columns and after data cleaning it was reduced to 40395 rows (observations) and 18 columns.

* In order to get geographical informations about the data, Postal Codes dataset from [https://data.gov.be/](https://data.gov.be/fr/dataset/328ba4f140ba0e870dfc9c70635fe7c1840980b1) is merged with  the real estate dataset during a previous BeCode [Real Estate Data analysis](https://github.com/kaiyungtan/Real-Estate-data-analysis).


## Data Preparation

* After further data cleaning, the dataset was reduced to 24040 rows (observations) with 19 columns.(belgium_real_estate_2020_rev1_19.11.2020.csv)

* Then the dataset were seperated to 2 dataset seperately namely df_house for houses and df_apartment for apartements.[Belgium_Real_Estate_2020](https://github.com/kaiyungtan/ImmoEliza-API/blob/main/notebook/Belgium_Real_Estate_2020_Immoweb%20-%20House%20%26%20Apartment.ipynb)

	- df_house (10254 rows, 19 columns)(belgium_houses_20.11.2020.csv)
	- df_apartment (13207 rows, 18 columns) (belgium_apartments_20.11.2020.csv')

*  to compare predicted price square per meter with the average price square per meter of a city, a seperate dataset was prepared to have only 7 columns:[Price_Sqm](https://github.com/kaiyungtan/ImmoEliza-API/blob/main/notebook/Data_analysis%20%26%20Create%20Price_Sqm.ipynb)
		- city_name	
		- postal_code	
		- price_sqm	
		- region	
		- province	
		- longitude	
		- lattitude

* 2 folium map were created to show average price square per meter in each city for houses and apartement. 
	* [average_house_price](https://immoeliza-real-estate.herokuapp.com/map_average_house_price)
	* [average_apartment_price](https://immoeliza-real-estate.herokuapp.com/map_average_apartment_price)


### Features of the dataset:
<ol>
	<li> postal_code (str): Postal code of city.</li>
	<li> city_name (str): city names in Belgium.</li>
	<li> number_of_rooms (int): The number of rooms of the property.</li>
	<li> house_area (int): The area (m2) of the house (floors).</li>
	<li> fully_equipped_kitchen (str): yes/no </li>
	<li> open_fire (str): yes/no </li>
	<li> terrace (str): yes/no </li>
	<li> garden (str): yes/no </li>
	<li> number_of_facades (int): The number of facades (0 to 4). </li>
	<li> swimming_pool (str): yes/no </li>
	<li> state_of_the_building (str): as new/good/just renovated/to renovate/unknown </li>
	<li> construction_year (int): The property built's year. </li>
	<li> surface_of_the_land (int): The area (m2) of the land. (for house only) </li>
</ol>

### Target of the dataset:

<ol>
<li> price (float) : Price (€) of the property.</li> 
</ol>

## Modeling

*  The objective of machine learning is not a model that does well on training data, but one that demonstrates it satisfies the business need and can be deployed on live data.

* A machine learning model is a file that has been trained to recognize certain types of patterns. You train a model over a set of data, providing it an algorithm that it can use to reason over and learn from those data.

* Libraries used in this project as follow:
	<details>
	  <summary>Libraries</summary>
			<li> from sklearn.model_selection import train_test_split</li> 
			<li> from sklearn.preprocessing import StandardScaler,OneHotEncoder</li> 
			<li> from sklearn.compose import ColumnTransformer</li> 
			<li> from sklearn.pipeline import Pipeline</li> 
			<li> from sklearn.linear_model import LinearRegression</li> 
			<li> from sklearn.linear_model import Lasso,Ridge,ElasticNet</li> 
			<li> from sklearn.tree import DecisionTreeRegressor</li> 
			<li> from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor </li> 
			<li> from xgboost import XGBRegressor</li> 
			<li> from sklearn.metrics import mean_squared_error, r2_score </li>  
	</details>

* The following diagram shows the process of modeling. 

![image](https://user-images.githubusercontent.com/69633814/100377837-5778a100-3012-11eb-958d-5e5862ffb533.png)

* random search cross validation were used to find the best parameter setting that gave the best results on the hold out data.

* Libraries used as follow:
	* from sklearn.model_selection import RandomizedSearchCV
	* from sklearn.metrics import make_scorer


## Evaluation

*  After evaluating 8 different models on the test set plus various random search cross validation conducted on the test set:   

	* a ridge model (alpha=0.7) was selected for house price prediction with train accuracy: 0.77 and test accuracy: 0.73.

	* a XGboost model (n_estimators=700, max_depth= 4, learning_rate= 0.3) was selected for apartment price prediction with train accuracy: 0.88 and test accuracy: 0.77

* plot predicted vs actual overlay the regression line as show for ridge model.

![ridge](https://user-images.githubusercontent.com/69633814/100383137-36697d80-301d-11eb-8f7e-685246ba39b0.png)

* plot predicted vs actual overlay the regression line as show for Xgboost model.

![xgb_rs](https://user-images.githubusercontent.com/69633814/100444604-f8676a80-30ab-11eb-967c-ba73005aabd1.png)

* models was saved using joblib library.

* to test a new / live unseen data, an example of new immoweb were chosen:

* https://www.immoweb.be/en/classified/house/for-sale/averbode/3271/9040949?searchId=5fb6439b8044e

	<details>
	  <summary>House for sale</summary>
			<li> €230,000</li> 
			<li> 4 bedrooms  226 m²square meters</li> 
			<li> Bredestraat 70 3271 — Averbode</li> 
			<li> Construction year 1930</li> 
			<li> Building condition To renovate</li> 
			<li> Facades 3</li> 
			<li> Kitchen type Installed</li> 
			<li> Surface of the plot 398 m²square meters</li> 
			<li> Garden surface 150 m²square meters</li> 
			<li> Terrace surface 25 m²square meters</li> 
	</details>

* create X_new features for predictions
	* X_new = {
	'postal_code':'3271',
	'number_of_rooms': 4,
	'house_area' : 226,
	'fully_equipped_kitchen': 'yes',
	'open_fire':'no',
	'terrace':'yes',
	'garden':'yes',
	'number_of_facades': 3,
	'swimming_pool': 'no',
	'state_of_the_building': 'to renovate',
	'construction_year' : 1930,
	'surface_of_the_land' : 398}

* The result show predicted price for the house is € 228964.0
and -0.45 % difference compare to the posted asking price for the house.

![image](https://user-images.githubusercontent.com/69633814/100384970-b691e200-3021-11eb-9979-0cf1fb82e7f9.png)

## Deployment on Heruko

* Create web app using Flask as framework
	* Create a virtual environment called myenv 
	* pip install all libraries flask / numpy etc
	* pip freeze --local > requirements.txt to create list of libraries installed on myenv environment
	* Create a flask app -- named app.py
	* Add routes for api
	* create layout template
	* create Procfile -- web: gunicorn app:app
	* pip install gunicorn and update requirements.txt
* Commit code on github
* To deploy in heruko:
	* create account in heroku
	* link the github to heroku
	* using terminal:
		* heroku create
		* git push heroku HEAD:master
		* heroku ps:scale web=1
		* heroku open
* Deployment successful.  

* To test a new unseen data, an example from immoweb is chosen:

* https://www.immoweb.be/en/classified/apartment/for-sale/anderlecht/1070/9042073?searchId=5fb749cc3354c

	<details>
	  <summary>Apartment for sale</summary>
		<li>€320,000</li> 
		<li>3 bedrooms | 130 m² square meters</li> 
		<li> 1070 — Anderlecht</li> 
		<li>Construction year	2017</li> 
		<li>Building condition	As new</li> 
		<li>Facades	2</li> 
		<li>Kitchen type	USA hyper equipped</li> 
		<li>Terrace surface	14 m² square meters</li> 
	 </details>

* Prediction with Postal Code - Apartment https://immoeliza-real-estate.herokuapp.com/apartment_postal_code

<img width="1143" alt="Screenshot 2020-11-26 at 19 02 01" src="https://user-images.githubusercontent.com/69633814/100381998-9a3e7700-301a-11eb-8f40-7161681a2cf5.png">

* Result the predicted price for the apartment is € 324,034 and 1.3 % difference compare to the posted asking price for the apartment.
<img width="1166" alt="Screenshot 2020-11-26 at 19 00 59" src="https://user-images.githubusercontent.com/69633814/100381829-2308e300-301a-11eb-86d4-1296780b902c.png">


## API for web dev

* two API routes were created for web dev to access the api namely:

	* https://immoeliza-real-estate.herokuapp.com/predict_house_tojson2
	* https://immoeliza-real-estate.herokuapp.com/predict_apartment_tojson2

* it returns a json file with 4 key value pairs:

	* "1. predicted price" : str(output)
    * "2. predicted price_sqm" : str(pricem2)
    * "3. {city_name} average price_sqm" : str(price_sqm)
    * "4. difference(%)" : str(difference_pct)


* tested api with [postman](https://www.postman.com)

![api_web_dev](https://user-images.githubusercontent.com/69633814/100384809-556a0e80-3021-11eb-968c-9deaeae8466f.png)


## Challenges

* time spent on training models
* deployment on heruko


## Limitation

* only for prediction price of general houses or apartments, it doesn't include subtype of property like villa,town-house,mansion,other exceptional property, country house.

* when unseen data is one of the subtype of property, the model predicted price will have higher difference of the price.


## Further Development

* To obtain more recent dataset from immoweb or other property websites  
* To include other features:

	*	Amenities : cellar? attic? parking?
	*	View of the property
	* 	Energy class
	*	Number of floors (for apartment)
	*	Elevator (for apartment)

* Explore other machine algorithms i.e CatBoost, LightGBM
* To propose related property on the website based on the inputs and predicted price
* To predict rental prices of houses or apartments
* Deployment model in virtual service in the cloud: 
	* Amazon Web Services (AWS) EC2 Instance   
	* Google Cloud platform 
	* Azure Cloud

* To include range of prediction i.e 10% lower or higher of the predicted price

<img width="1155" alt="Screenshot 2020-11-27 at 14 17 39" src="https://user-images.githubusercontent.com/69633814/100453566-71ba8980-30bb-11eb-9823-8fd44b609d8a.png">


