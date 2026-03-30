import numpy as np

def eucDistanceSqaured(point_1, point_2):
    x_squared = (point_1[0] - point_2[0]) ** 2
    y_squared = (point_1[1] - point_2[1]) ** 2
    return (x_squared + y_squared)

class KMeans:
    def __init__(self, k, cities):
        self.k = k
        self.cities = cities[['lat','lng']].values
        #initialise k random centroids
        indices = np.random.permutation(len(cities))
        centroid_indices = indices[:k]
        self.centroids = cities.iloc[centroid_indices][['lat', 'lng']].values
        
    def assign(self):
        #create (/reset) k arrays, for the locations of all assigned cities in each cluster
        self.clusters = [[] for _ in range(self.k)]
        for city in self.cities:
            max_distance = float('inf')
            cluster_id = -1
            for i, centroid in enumerate(self.centroids):
                distance = eucDistanceSqaured(city, centroid)
                if distance < max_distance:
                    max_distance = distance
                    cluster_id = i
            self.clusters[cluster_id].append(city)
                
            
                    



