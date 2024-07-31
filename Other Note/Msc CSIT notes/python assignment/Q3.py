import numpy as np

class Perceptron:
    def __init__(self, num_features, learning_rate=0.01, num_epochs=100):
        self.weights = np.zeros(num_features + 1)
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs
    
    def predict(self, x):
        # Add bias term to input
        x = np.append(x, 1)
# Compute dot product of weights and input
        z = np.dot(self.weights, x)
        # Apply step function to dot product
        if z > 0:
            return 1
        else:
            return 0
    
    def train(self, X, y):
        for epoch in range(self.num_epochs):
            for i in range(X.shape[0]):
                # Add bias term to input
                x = np.append(X[i], 1)
                # Compute dot product of weights and input
                z = np.dot(self.weights, x)
                # Apply step function to dot product
                y_pred = 1 if z > 0 else 0
                # Update weights based on prediction error
                error = y[i] - y_pred
                self.weights += self.learning_rate * error * x

# Given training set
X_train = np.array([[5.9, 75], [5.8, 86], [5.2, 50], [5.4, 55], [6.1, 85], [5.5, 62]])
y_train = np.array([1, 1, 0, 0, 1, 0])

# Train perceptron on training set
perceptron = Perceptron(num_features=2)
perceptron.train(X_train, y_train)

# Inputs to predict class for
x_input1 = np.array([6, 82])
x_input2 = np.array([5.3, 52])

# Predict class for inputs
y_pred1 = perceptron.predict(x_input1)
y_pred2 = perceptron.predict(x_input2)

print("Input 1: ", x_input1)
print("Predicted class for input 1: ", y_pred1)

print("Input 2: ", x_input2)
print("Predicted class for input 2: ", y_pred2)
