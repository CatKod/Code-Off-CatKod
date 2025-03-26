import tensorflow as tf
import numpy as np

# Define the neural network model
class NeuralNetwork(tf.keras.Model):
    def __init__(self, hidden_size):
        super(NeuralNetwork, self).__init__()
        self.hidden_layer = tf.keras.layers.Dense(hidden_size, activation='sigmoid')
        self.output_layer = tf.keras.layers.Dense(1, activation='sigmoid')

    def call(self, inputs):
        x = self.hidden_layer(inputs)
        return self.output_layer(x)

# Train the neural network
def train_neural_network(X, Y, hidden_size, num_iterations, learning_rate):
    model = NeuralNetwork(hidden_size)
    model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
                  loss='binary_crossentropy')

    # Train the model
    model.fit(X, Y, epochs=num_iterations, verbose=0)

    return model

# Example usage
if __name__ == "__main__":
    # Example dataset (input features and labels)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)  # Input features
    Y = np.array([[0], [1], [1], [0]], dtype=np.float32)  # Labels

    # Train the neural network
    model = train_neural_network(X, Y, hidden_size=4, num_iterations=10000, learning_rate=0.1)

    # Test the neural network
    predictions = model.predict(X)
    predictions = (predictions > 0.5).astype(int)
    print("Predictions:", predictions)
