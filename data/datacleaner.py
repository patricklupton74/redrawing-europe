#objectives:
#keep only cities in europe ()
#keep only city, country, lng, lat attributes (✓)
import pandas as pd

usecols = ['city','lat','lng','country']

cities = pd.read_csv("data/worldcities.csv", index_col = 0,usecols = usecols)
cities.to_csv("data/onlycorrectcolumns.csv")

