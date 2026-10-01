import numpy as np

def linear_regression_gradient_descent(X, y, alpha, iterations):
    X = np.asarray(X)
    y = np.asarray(y)
    
    m, n = X.shape
    theta = np.zeros(n)
    
    for _ in range(iterations):
        # h_theta(X) = X @ theta
        predictions = X @ theta
        
        # Gradient = (1 / m) * X^T @ (predictions - y)
        gradient = (1 / m) * (X.T @ (predictions - y))
        
        # Gradient descent update
        theta = theta - alpha * gradient
        
    return theta