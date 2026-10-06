import numpy as np
def make_diagonal(x):
	x=np.asarray(x)
	rev=np.diag(x)
	return rev.tolist()