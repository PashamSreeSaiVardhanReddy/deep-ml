import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    X = np.asarray(features)
    y = np.asarray(labels)
    w = np.asarray(weights)
    
    # Linear combination: z = Xw + bias
    z = X @ w + bias
    
    # Sigmoid activation: 1 / (1 + e^(-z))
    probabilities = np.round(1.0 / (1.0 + np.exp(-z)), 4)
    
    # Mean Squared Error: mean((probabilities - y)^2)
    mse = float(np.round(np.mean((probabilities - y) ** 2), 4))
    
    return probabilities.tolist(), mse