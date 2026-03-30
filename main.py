import pandas as pd
import numpy as np
from algorithms.knn import KNN

cities = pd.read_csv("data/europeancities.csv")

#kNN training/input set splitting
indices = np.random.permutation(len(cities))
train_size = 0.8
train_count = int(len(cities) * train_size)

input_indices = indices[train_count:]
train_indices = indices[:train_count]

train = cities.iloc[train_indices]
input = cities.iloc[input_indices]

pos_training = train[['lat', 'lng']].values
label_training = train['country'].values

pos_input = input[['lat', 'lng']].values
label_input = input['country'].values

knn = KNN(5)
knn.train(pos_training, label_training)
predictions = knn.predict(pos_input)

#accuracy rating
correct = 0 
for i, prediction in enumerate(predictions):
    if prediction == label_input[i]:
        correct += 1
accuracy = (correct / len(label_input)) * 100

print(f"{accuracy}%")

print(f"k: {knn.k}")
print(f"Training size: {len(pos_training)}")
print(f"Input size: {len(pos_input)}")
