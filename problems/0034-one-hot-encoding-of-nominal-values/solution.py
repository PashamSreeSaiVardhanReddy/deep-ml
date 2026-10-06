import numpy as np
def to_categorical(X,n_col=None):
	X=np.asarray(X)
	if n_col==None:
		n_col=int(np.max(X))+1 if X.size>0 else 0 
	return np.eye(n_col)[X]
