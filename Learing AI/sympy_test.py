from sympy import symbols, diff
import numpy as np

# Define the variable
Y, x = symbols('Y x')
# Define the function
f = Y**2 + 2*Y*x + np.exp(2*Y)
# Compute the derivative with respect to Y
f_prime = diff(f, Y)
# Display the result
print(f"Derivative of f with respect to Y: {f_prime}")