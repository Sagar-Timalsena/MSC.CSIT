class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
    
    def predict(self, inputs):
        # Calculate the weighted sum of inputs and add bias
        weighted_sum = 0
        for i in range(len(inputs)):
            weighted_sum += inputs[i] * self.weights[i]
        weighted_sum += self.bias
        
        # Apply threshold activation function
        if weighted_sum >= 0:
            return 1
        else:
            return 0
        
weights = [0.5, -0.3, 0.2]
bias = -0.1
neuron = Neuron(weights, bias)

inputs = [1, 0, 0]
output = neuron.predict(inputs)
print(output)  # Expected output: 1        
