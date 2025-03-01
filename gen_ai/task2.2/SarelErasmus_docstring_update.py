import pandas as pd
import numpy as np

K_NEIGHBORS = 8

def findMajority(arr):
  count = 1
  current_major = arr[0]

  for element in arr[1:]:
    if count == 0:
      current_major = element
      count = 1
    elif element == current_major:
      count += 1
    else:
      count -= 1
  
  return current_major

train_data = pd.read_csv('MNIST_training.csv')
test_data = pd.read_csv('MNIST_test.csv')

train_data_y = train_data.iloc[:, 0]
train_data_X = train_data.drop('label', axis=1)

test_data_y = test_data.iloc[:, 0]
test_data_X = test_data.drop('label',axis=1)

correct_predictions = 0 

for test_point in range(len(test_data_X)):
  dist = [] 

  for train_point in range(len(train_data_X)):
    dist.append(0)

    matrix = np.subtract(test_data_X.iloc[test_point,:],train_data_X.iloc[train_point,:])
    matrix = np.multiply(matrix,matrix)
    dist[train_point] = np.sqrt(np.sum(matrix))

  nearest_neighbors = np.argpartition(dist,K_NEIGHBORS)[:K_NEIGHBORS]
  nearest_neighbors = np.array(train_data_y[nearest_neighbors])  

  if findMajority(nearest_neighbors) == test_data_y[test_point]:
    correct_predictions += 1

print('K =', K_NEIGHBORS, 'Nearest Neighbor:')
print('Correctly Predicted Labels: ',correct_predictions)
print('Incorrectly Predicted Labels: ',len(test_data_y)-correct_predictions)
print('Accuracy: ',correct_predictions/len(test_data_y))