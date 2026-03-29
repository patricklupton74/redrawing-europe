import heapq

def eucDistanceSqaured(point_1, point_2):
    x_squared = (point_1[0] - point_2[0]) ** 2
    y_squared = (point_1[1] - point_2[1]) ** 2
    return (x_squared + y_squared)

class KNN:
    def __init__(self, k):
        self.k = k

    def train(self, pos_training, label_training):
       #pos_training = array of positions of cities in training set
       #label_training = array of countries of cities in training set
       self.pos_training = pos_training
       self.label_training = label_training

    def predict(self, pos_input):
        #pos_input = array of positions of input cities, waiting to be assigned
        predictions = []
        for city_input in pos_input:
            #extract k nearest neighbours using heap
            heap  = []
            training_progress = 0
            for city_training in self.pos_training:
                #push k first training nodes to heap
                if training_progress < self.k:
                    heapq.heappush(heap, ((-1) * (eucDistanceSqaured(city_input, self.pos_training[training_progress])), self.label_training[training_progress]))
                #check if remaining cities have a smaller distance than the max distance in heap, if so then replace max
                else:  
                    if eucDistanceSqaured(city_input, self.pos_training[training_progress]) < (-1) * heap[0][0]:
                        heapq.heapreplace(heap, ((-1) * eucDistanceSqaured(city_input, self.pos_training[training_progress]), self.label_training[training_progress]))
                training_progress += 1
            
            #find most common label in heap
            labels = [label for _, label in heap]
            prediction = max(set(labels), key=labels.count)
            predictions.append(prediction)
        return predictions
            
                



