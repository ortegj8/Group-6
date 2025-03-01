import pandas as pd
import numpy as np

# Number of neighbors to consider in KNN
K_NEIGHBORS = 8

def findMajority(arr):
    """
    Determines the majority element in the given array using the Boyer-Moore Voting Algorithm.
    
    Parameters:
    arr (list): List of elements (labels of nearest neighbors)
    
    Returns:
    int: The majority element in the list
    """
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

# Load training and test data from CSV files
train_data = pd.read_csv('MNIST_training.csv')
test_data = pd.read_csv('MNIST_test.csv')

# Separate features and labels for training data
train_data_y = train_data.iloc[:, 0]  # Labels
train_data_X = train_data.drop('label', axis=1)  # Features

# Separate features and labels for test data
test_data_y = test_data.iloc[:, 0]  # Labels
test_data_X = test_data.drop('label', axis=1)  # Features

# Initialize the counter for correct predictions
correct_predictions = 0 

# Loop through each test sample
for test_point in range(len(test_data_X)):
    dist = []  # List to store distances between test sample and all training samples

    # Compute Euclidean distance from current test sample to each training sample
    for train_point in range(len(train_data_X)):
        dist.append(0)
        matrix = np.subtract(test_data_X.iloc[test_point, :], train_data_X.iloc[train_point, :])  # Difference
        matrix = np.multiply(matrix, matrix)  # Square the differences
        dist[train_point] = np.sqrt(np.sum(matrix))  # Compute the Euclidean distance

    # Find the indices of the K nearest neighbors
    nearest_neighbors = np.argpartition(dist, K_NEIGHBORS)[:K_NEIGHBORS]
    nearest_neighbors = np.array(train_data_y[nearest_neighbors])  # Retrieve corresponding labels

    # Predict label by majority voting
    if findMajority(nearest_neighbors) == test_data_y[test_point]:
        correct_predictions += 1

# Print results
print('K =', K_NEIGHBORS, 'Nearest Neighbor:')
print('Correctly Predicted Labels:', correct_predictions)
print('Incorrectly Predicted Labels:', len(test_data_y) - correct_predictions)
print('Accuracy:', correct_predictions / len(test_data_y))