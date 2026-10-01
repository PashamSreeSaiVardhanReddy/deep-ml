import numpy as np
def transform_basis(b,c):
	b=np.asarray(b)
	c=np.asarray(c)
	c_inv=np.linalg.inv(c)
	p=c_inv @ b
	return p