<img align="center" alt="ImmoEliza Logo" title="ImmoEliza Logo" width="100px" 
src="https://user-images.githubusercontent.com/69633814/100371617-5a6e9400-3008-11eb-818f-c4fbee59744a.png" />

# ImmoEliza-API

To create an API that will make price forecasts on houses according to certain parameters (postal code, number of rooms, surface area, etc.)

* Website - https://immoeliza-real-estate.herokuapp.com/

* Github page - https://kaiyungtan.github.io/ImmoEliza-API/


## Background

This project is a collaboration between BeCode AI and the BeCode Web 
Dev team.

The AI developers will create an API and the web developers will develop an interface for the client "ImmoEliza". 

The main process is about a collaboration between the AI and the web dev so that all have to be in sync in order to know how to construct the form.

Team Members consists of: 

* Web Dev : Valentin, Henrique, Nathanaël 

* AI Dev 	: Adam 

    
## Mission objectives  

* Be able to create a prediction model
* Be able to deploy model
* Be able to work in a team
* Be able to build an api

## The Mission

You need to create an API that will make price forecasts on houses according to certain parameters (Zip code, number of rooms, surface area, etc...). This API will be used by web devs who will be able to use it to create an interface for the ImmoEliza agency.


### Must-have features

* The api must be functional 
* Your model must be functional


### Additional features

* to provide house/apartment average price (square per meter) for all cities in Belgium
* to show the difference (%) between house/apartment sq/m2 versus the average sq/m2 for the city


## Process Overview

![image](https://user-images.githubusercontent.com/69633814/100321235-a696e580-2fc2-11eb-9f09-36423760b5b4.png)

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

* Then the dataset were seperated to 2 dataset seperately namely df_house for houses and df_apartment for apartements.(Belgium_Real_Estate_2020_Immoweb - House & Apartment.ipynb)

	- df_house (10254 rows, 19 columns)(belgium_houses_20.11.2020.csv)
	- df_apartment (13207 rows, 18 columns) (belgium_apartments_20.11.2020.csv')

*  to compare predicted price square per meter with the average price square per meter of a city, a seperate dataset was prepared to have only 7 columns:(Data_analysis & Create Price_Sqm.ipynb)
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

	* from sklearn.model_selection import train_test_split
	* from sklearn.preprocessing import StandardScaler,OneHotEncoder
	* from sklearn.compose import ColumnTransformer
	* from sklearn.pipeline import Pipeline
	* from sklearn.linear_model import LinearRegression
	* from sklearn.linear_model import Lasso,Ridge,ElasticNet
	* from sklearn.tree import DecisionTreeRegressor
	* from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor 
	* from xgboost import XGBRegressor
	* from sklearn.metrics import mean_squared_error, r2_score  

* The following diagram shows the process of modeling. 

![image](https://user-images.githubusercontent.com/69633814/100377837-5778a100-3012-11eb-958d-5e5862ffb533.png)

* random search cross validation were used to find the best parameter setting that gave the best results on the hold out data.

* Libraries used as follow:
	* from sklearn.model_selection import RandomizedSearchCV
	* from sklearn.metrics import make_scorer


## Evaluation

*  After evaluating 8 models run on the test set, a ridge model (Linear least squares with l2 regularization) was selected for house price prediction. 
* Train accuracy: 0.77 Test accuracy: 0.73

* model was saved using joblib library.

* to test a new / live unseen data, an example of new immoweb were chosen:

https://www.immoweb.be/en/classified/house/for-sale/averbode/3271/9040949?searchId=5fb6439b8044e

* House for sale
* €230,000
* 4 bedrooms  226 m²square meters
* Bredestraat 70 3271 — Averbode
* Construction year 1930
* Building condition To renovate
* Facades 3
* Kitchen type Installed
* Surface of the plot 398 m²square meters
* Garden surface 150 m²square meters
* Terrace surface 25 m²square meters


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

![image](https://user-images.githubusercontent.com/69633814/100379623-762c6700-3015-11eb-937f-c9eb76935394.png)



## Deployment

*  

## Challenges

*  


## Limitation

*  

## Further Development

*  




