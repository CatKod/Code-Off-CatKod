import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset from CSV file
df = pd.read_csv('test_house_prices.csv')

# Preprocess data: Select relevant columns and handle missing values
df = df[['Vị trí 1', 'Vị trí 2', 'Vị trí 3', 'Vị trí 4']].dropna()

# Convert columns to numeric
df = df.apply(pd.to_numeric, errors='coerce').dropna()

# Define input (X) and output (y)
X = df[['Vị trí 1', 'Vị trí 2', 'Vị trí 3']]
y = df['Vị trí 4']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Predict for a new data point
new_data = np.array([[300000, 150000, 100000]])  # Example input
predicted_value = model.predict(new_data)
print("Predicted Value for new data:", predicted_value[0])
