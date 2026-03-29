#objectives:
#keep only cities in europe (removed trans-continental and cyprus) (✓)
#keep only city, country, lng, lat attributes (✓)
#remove tiny microstates (✓)

import pandas as pd

usecols = ['city','lat','lng','country','population']

cities = pd.read_csv("data/worldcities.csv", usecols = usecols)
cities.to_csv("data/onlycorrectcolumns.csv", index = False)

'''
for country in cities["country"].unique():
   print(country)
'''

european_countries = [
    "Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina",
    "Bulgaria", "Croatia", "Czechia", "Denmark", "Estonia",
    "Finland", "France", "Germany", "Greece", "Hungary", "Ireland",
    "Italy", "Latvia", "Lithuania", "Luxembourg",
    "Malta", "Moldova", "Montenegro", "Netherlands", "North Macedonia",
    "Norway", "Poland", "Portugal", "Romania", "Serbia",
    "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine",
    "United Kingdom"
]

cities = cities[cities["country"].isin(european_countries)]
cities = cities.groupby("country").apply(lambda x: x.nlargest(min(len(x), 100), 'population')).reset_index(drop = False)
cities = cities.drop(columns=['level_1'])
cities.to_csv("data/europeancities.csv", index = False)
#print(cities.head())
#print(cities.columns)