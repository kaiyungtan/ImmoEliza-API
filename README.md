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
 
- **postal_code** *str*: Postal code of city.
- **city_name** *str*: city names in Belgium.
- **number_of_rooms** *int*: The number of rooms of the property.
- **house_area** *int*: The area (m2) of the house (floors).
- **fully_equipped_kitchen** *str*: yes/no 
- **open_fire***str*: yes/no
- **terrace** *str*: yes/no
- **garden** *str*: yes/no
- **number_of_facades** *int*: The number of facades (0 to 4).
- **swimming_pool** *str*: yes/no
- **state_of_the_building** *str*: as new/good/just renovated/to renovate/unknown
- **construction_year** *int*: The property built's year.
- **surface_of_the_land** *int*: The area (m2) of the land.
 
Our target is:

- **price** *float*: Price (€) of the property.

</details>

## Process Overview

![image](https://user-images.githubusercontent.com/69633814/100321235-a696e580-2fc2-11eb-9f09-36423760b5b4.png)

## Business Understanding 


* The dataset for the real estate were scrapped form Immoweb in September 2020 with more than 50,000 of properties including houses and apartments.

* Data cleaning and analysis were done on this dataset. [Real Estate Data analysis](https://github.com/kaiyungtan/Real-Estate-data-analysis)

* 11 features

* Price prediction of the real estate involves a lot of uncertain.

## Data Understanding

*  

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

*  Limit 

## Further Development

*  




