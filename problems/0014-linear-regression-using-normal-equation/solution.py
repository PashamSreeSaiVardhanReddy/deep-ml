import numpy as np
def linear_regression_normal_equation(X,y):
	X=np.asarray(X)
	y=np.asarray(y)
	theta=np.linalg.inv(X.T @ X) @ X.T @ y
	return theta.tolist()