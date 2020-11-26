# ImmoEliza-API

To create an API that will make price forecasts on houses according to certain parameters (Zip code, number of rooms, surface area, etc.)

Deployment through Heroku - https://immoeliza-real-estate.herokuapp.com/


## Background

This project is a collaboration between BeCode AI and the BeCode Web 
Dev team.

The AI developers will create an API and the web developers will develop an interface for the client "ImmoEliza". 

The main process is about a collaboration between the AI and the web dev so that all have to be in sync in order to know how to construct the form.

Team Members consists of: 

Web Dev : Valentin, Henrique, Nathanaël 

AI Dev 	: Adam 

    
## Mission objectives  

- [X] Be able to create a prediction model
- [X] Be able to deploy model
- [X] Be able to work in a team
- [X] Be able to build an api

## The Mission

You need to create an API that will make price forecasts on houses according to certain parameters (Zip code, number of rooms, surface area, etc...). This API will be used by web devs who will be able to use it to create an interface for the ImmoEliza agency.


### Must-have features

- [X] The api must be functional 
- [X] Your model must be functional


### Additional features

- [X] to provide house/apartment average price (square per meter) for all cities in Belgium
- [X] to show the difference (%) between house/apartment sq/m2 versus the average sq/m2 for the city



<details>
  <summary>Features of the dataset</summary>
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
Our target is:

- **price** *float*: Price (€) of the property. 

</details>

## Process Overview

![image](https://user-images.githubusercontent.com/69633814/100321235-a696e580-2fc2-11eb-9f09-36423760b5b4.png)

## Business Understanding 

* Prediction of a real estate price is not an easy task. It involves a lot of variables. The owner of the real estate determine the price based on many factors. The property itself is of course the main factor to set the price. However the location and facilities around the property can hughly impact the price. In addition, the economy situation or inflation of the country also play a part in influencing the price.

* In this project, we are using machine learning to learn from the features of the real estate to price the price. It was constrainted to the features selected by the models. It neither take into account of the facilities around the real estate , nor it include the factor of COVID-19 effect on the housing price.

## Data Understanding

* The dataset for the real estate were scrapped form [Immoweb](https://www.immoweb.be/) probably the biggest real estate website in Belgium mid of September 2020 with more than 50,000 of properties including houses and apartments.

* Data cleaning and analysis were done on this dataset. [Real Estate Data analysis](https://github.com/kaiyungtan/Real-Estate-data-analysis)

* Initially the dataset have 52077 rows and 20 columns and after data cleaning it was reduced to 40395 rows (observations) and 18 columns.

* In order to build machine models from this dataset, the dataset were seperated to 2 dataset seperately namely df_house for house and df_apartment for apartement.

* df_house has 12 features while df_apartment has 11 features.  


## Data Preparation

*  

## Modeling

*  

## Evaluation

*  


## Deployment

*  

## Challenges

*  


## Limitation

*  

## Further Development

*  




