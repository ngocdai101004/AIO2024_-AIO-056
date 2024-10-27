import numpy as np

class CustomLinearRegression:
    def __init__(self, X_data, y_target, learning_rate=0.01, epochs=6000):
        self.X = np.concatenate((np.ones((X_data.shape[0], 1)), X_data), axis=1)  # Adding bias term (intercept)
        self.y = y_target.reshape(-1, 1)  # Ensure y is a column vector
        self.num_features = self.X.shape[1] 
        self.num_samples = X_data.shape[0]
        self.learning_rate = learning_rate
        self.epochs = epochs

        # Initialize weights
        self.weights = np.random.randn(self.num_features, 1)
        self.losses = []
    
    def compute_loss(self, y_pred, y_true):
        return np.mean((y_pred - y_true) ** 2)
    
    def fit(self):
        for epoch in range(self.epochs):
            # Prediction
            y_pred = np.dot(self.X, self.weights)

            # Loss computation
            loss = self.compute_loss(y_pred, self.y)
            self.losses.append(loss)
            
            # Gradient calculation
            gradient = np.dot(self.X.T, (y_pred - self.y)) / self.num_samples
            # Update weights
            self.weights -= self.learning_rate * gradient

            if (epoch + 1) % 500 == 0:
                print(f"Epoch {epoch}, Loss: {loss}")

        return {
            "loss": sum(self.losses) / len(self.losses),  # Return average loss
            "weights": self.weights,
        }
    
    def predict(self, X):
        X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)  # Add bias term
        y_pred = np.dot(X, self.weights)
        return y_pred.reshape(-1)
