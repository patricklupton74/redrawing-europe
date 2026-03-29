#objectives:
#keep only cities in europe (removed trans-continental and cyprus) (✓)
#keep only city, country, lng, lat attributes (✓)
#remove tiny microstates (✓)

import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


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
cities = cities[~cities['city'].isin(['Ciudad de Melilla', 'Ciudad de Ceuta'])]
cities.to_csv("data/europeancities.csv", index = False)
#print(cities.head())
#print(cities.columns)


fig, ax = plt.subplots(figsize=(12, 8), subplot_kw={'projection': ccrs.PlateCarree()})

ax.add_feature(cfeature.LAND, facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
ax.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
ax.add_feature(cfeature.COASTLINE, linewidth=0.5)

ax.scatter(cities['lng'], cities['lat'], s=2, color='red', transform=ccrs.PlateCarree())

ax.set_extent([-25, 45, 34, 72])

plt.show()

