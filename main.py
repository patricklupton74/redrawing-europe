import pandas as pd
from algorithms.knn import KNN
from utils import train_test_split

cities = pd.read_csv("data/europeancities.csv")

#kNN --------------------------------------------------------------------------------------
train_size = 0.2
pos_training, label_training, pos_input, label_input =train_test_split(cities, train_size)

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
#------------------------------------------------------------------------------------------