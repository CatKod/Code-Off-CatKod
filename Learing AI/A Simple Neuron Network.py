import numpy as np

# Sigmoid activation function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Derivative of the sigmoid function
def sigmoid_derivative(z):
    return sigmoid(z) * (1 - sigmoid(z))

# Initialize parameters
def initialize_parameters(input_size, hidden_size, output_size):
    np.random.seed(1)
    W1 = np.random.randn(hidden_size, input_size) * 0.01
    b1 = np.zeros((hidden_size, 1))
    W2 = np.random.randn(output_size, hidden_size) * 0.01
    b2 = np.zeros((output_size, 1))
    return W1, b1, W2, b2

# Forward propagation
def forward_propagation(X, W1, b1, W2, b2):
    Z1 = np.dot(W1, X) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)
    cache = (Z1, A1, Z2, A2)
    return A2, cache

# Compute cost
def compute_cost(A2, Y, m):
    cost = -np.sum(Y * np.log(A2) + (1 - Y) * np.log(1 - A2)) / m
    return np.squeeze(cost)

# Backward propagation
def backward_propagation(X, Y, cache, W2, m):
    Z1, A1, Z2, A2 = cache
    dZ2 = A2 - Y
    dW2 = np.dot(dZ2, A1.T) / m
    db2 = np.sum(dZ2, axis=1, keepdims=True) / m
    dZ1 = np.dot(W2.T, dZ2) * sigmoid_derivative(Z1)
    dW1 = np.dot(dZ1, X.T) / m
    db1 = np.sum(dZ1, axis=1, keepdims=True) / m
    return dW1, db1, dW2, db2

# Update parameters
def update_parameters(W1, b1, W2, b2, dW1, db1, dW2, db2, learning_rate):
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2
    return W1, b1, W2, b2

# Neural network model
def neural_network(X, Y, hidden_size, num_iterations, learning_rate):
    input_size = X.shape[0]
    output_size = Y.shape[0]
    W1, b1, W2, b2 = initialize_parameters(input_size, hidden_size, output_size)
    m = X.shape[1]

    for i in range(num_iterations):
        A2, cache = forward_propagation(X, W1, b1, W2, b2)
        cost = compute_cost(A2, Y, m)
        dW1, db1, dW2, db2 = backward_propagation(X, Y, cache, W2, m)
        W1, b1, W2, b2 = update_parameters(W1, b1, W2, b2, dW1, db1, dW2, db2, learning_rate)

        if i % 100 == 0:
            print(f"Iteration {i}, Cost: {cost}")

    return W1, b1, W2, b2

# Example usage
if __name__ == "__main__":
    # Example dataset (input features and labels)
    X = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])  # Input features
    Y = np.array([[0, 1, 1, 0]])  # Labels

    # Train the neural network
    W1, b1, W2, b2 = neural_network(X, Y, hidden_size=4, num_iterations=10000, learning_rate=0.1)

    # Test the neural network
    A2, _ = forward_propagation(X, W1, b1, W2, b2)
    predictions = (A2 > 0.5).astype(int)
    print("Predictions:", predictions)
