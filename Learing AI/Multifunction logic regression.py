from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
X = np.random.rand(100, 3)  # 100 samples, 3 features
y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Binary target based on a simple rule

# Transform the features to include polynomial terms of degree 3
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

# Split the transformed data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

# Initialize and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Visualize the data and decision boundary
def plot_decision_boundary(X, y, model):
    x_min, x_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
    y_min, y_max = X[:, 2].min() - 0.1, X[:, 2].max() + 0.1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    Z = model.predict(poly.transform(np.c_[xx.ravel(), yy.ravel(), np.zeros_like(xx.ravel())]))  # Assume higher features are zero
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.Paired)
    plt.scatter(X[:, 1], X[:, 2], c=y, edgecolor='k', cmap=plt.cm.Paired)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Decision Boundary')
    plt.show()

# Plot decision boundary using the first two features
plot_decision_boundary(X_test, y_test, model)
