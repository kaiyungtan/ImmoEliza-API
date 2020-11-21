import requests

url = 'http://localhost:5000/predict_house'
r = requests.post(url,json={'city_name': 'Averbode',
							'number_of_rooms': 4,
							'house_area' : 226,
							'surface_of_the_land' : 398,
							'fully_equipped_kitchen': 1,
							'open_fire':0,
							'terrace': 1,
							'garden': 1,
							'number_of_facades': 3,
							'swimming_pool': 0,
							'state_of_the_building': 'to renovate',
							'construction_year' : 1930,
							'province': 'Brabant flamand',
							'region': 'Flandre'})

print(r.json())

url = 'http://localhost:5000/predict_house_postal_code'
r = requests.post(url,json={'postal_code': '3271',
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
							'construction_year' : 1930})

print(r.json())

url = 'http://localhost:5000/predict_apartment'
r = requests.post(url,json={'city_name': 'Anderlecht',
							'number_of_rooms': 2,
							'house_area' : 130,
							'fully_equipped_kitchen': 1,
							'open_fire':0,
							'terrace': 1,
							'garden': 0,
							'number_of_facades': 2,
							'swimming_pool': 0,
							'state_of_the_building': 'as new',
							'construction_year' : 2017,
							'province': 'Bruxelles-Capitale',
							'region': 'Bruxelles'})

print(r.json())