import numpy as np
def calculate_matrix_mean(m,c):
	c=c.lower()
	if c=="column":
		n=0
	elif c=="row":
		n=1
	else:
		n=None
	# mean=np.mean(m[0],axis=n)
	return np.mean(m,axis=n).tolist()
