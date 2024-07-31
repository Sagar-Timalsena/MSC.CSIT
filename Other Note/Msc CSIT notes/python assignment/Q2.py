import numpy as np

# Define the training dataset for the AND gate
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

# Define the activation function
def activation(z):
    if z >= 0:
        return 1
    else:
        return 0

# Define the Perceptron Learning Algorithm
def perceptron_learning(X, y, eta, epochs):
    n, m = X.shape
    w = np.zeros(m)
    b = 0
    for epoch in range(epochs):
        for i in range(n):
            z = np.dot(w, X[i]) + b
            a = activation(z)
            error = y[i] - a
            w += eta * error * X[i]
            b += eta * error
    return w, b

# Train the AND gate using the Perceptron Learning Algorithm
w, b = perceptron_learning(X, y, eta=0.1, epochs=10)

# Test the trained model on the input [1, 1]
z = np.dot(w, [1, 1]) + b
a = activation(z)
print(a)  # Output: 1
