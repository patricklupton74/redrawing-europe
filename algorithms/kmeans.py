import numpy as np

class KMeans:
    def __init__(self, k, cities):
        self.k = k
        #create k arrays, for the locations of all assigned cities in each cluster
        self.clusters = [[] for _ in range(k)]
        #initialise k random centroids
        indices = np.random.permutation(len(cities))
        centroid_indices = indices[:k]
        self.centroids = cities.iloc[centroid_indices][['lat', 'lng']].values
        
    