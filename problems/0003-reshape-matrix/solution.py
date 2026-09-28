import numpy as np
def reshape_matrix(a,new_shape):
	a=np.asarray(a)
	if a.size != new_shape[0]*new_shape[1]:
		return []
	return a.reshape(new_shape).tolist()