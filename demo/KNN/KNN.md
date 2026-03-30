# K-Nearest Neighbours

Supervised algorithm that classifies each city by majority vote of its k nearest neighbours in the training set. Trained purely on lat/lng coordinates with no knowledge of political borders.

## Parameters
k -> Number of nearest neighbours considered  
t -> Training set size (e.g. 0.7 = 70% of European city dataset used for training, the rest is used as input)  
acc -> Measured accuracy for that instance