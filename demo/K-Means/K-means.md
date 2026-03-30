# K-Means

Unsupervised algorithm that groups cities into k clusters based purely on geographic proximity. Centroids are initialised randomly and iteratively repositioned until convergence.

K-Means is non-deterministic — results will differ on each run with the same k due to random centroid initialisation, as reflected in the demo images.

## Parameters
k -> Number of clusters (38 = one cluster per country in the dataset)