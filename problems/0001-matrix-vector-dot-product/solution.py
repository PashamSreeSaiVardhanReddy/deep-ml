import numpy as np
def matrix_dot_vector(a,b):
	if len(a)==0 or len(a[0])!=len(b):
		return -1
	b=np.asarray(b).reshape(-1,1)
	c=np.dot(a,b)
	return c.flatten().tolist()