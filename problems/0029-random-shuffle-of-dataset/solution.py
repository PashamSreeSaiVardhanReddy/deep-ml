import numpy as np

def shuffle_data(X, y, seed=None):
    if seed is not None:
        np.random.seed(seed)
        
    X = np.asarray(X)
    y = np.asarray(y)
    
    # Generate one shared permutation of indices
    indices = np.random.permutation(len(X))
    
    return X[indices], y[indices]