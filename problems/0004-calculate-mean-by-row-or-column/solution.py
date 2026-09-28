import numpy as np

def calculate_matrix_mean(m, c):
    c = c.lower()
    
    if c == "column":
        axis = 0
    elif c == "row":
        axis = 1
    else:
        axis = None
        
    return np.mean(m, axis=axis).tolist()