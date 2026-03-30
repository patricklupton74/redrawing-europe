# K-Nearest Neighbours

Supervised algorithm that classifies each city by majority vote of its k nearest neighbours in the training set. Trained purely on lat/lng coordinates with no knowledge of political borders.

## Parameters
k -> Number of nearest neighbours considered  
t -> Training set size (e.g. 0.8 = 80% of European city dataset used for training)  
acc -> Measured accuracy for that instance