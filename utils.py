
import numpy as np

def train_test_split(cities, train_size): 
    indices = np.random.permutation(len(cities))
    train_count = int(len(cities) * train_size)

    input_indices = indices[train_count:]
    train_indices = indices[:train_count]

    train = cities.iloc[train_indices]
    input = cities.iloc[input_indices]

    pos_training = train[['lat', 'lng']].values
    label_training = train['country'].values

    pos_input = input[['lat', 'lng']].values
    label_input = input['country'].values

    return pos_training, label_training, pos_input, label_input