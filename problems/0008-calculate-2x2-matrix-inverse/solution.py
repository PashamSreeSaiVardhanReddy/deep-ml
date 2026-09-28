import numpy as np
def inverse_2x2(m):
    det_m=np.linalg.det(m)
    if det_m==0:
        return None
    i_m=np.linalg.inv(m)
    return i_m