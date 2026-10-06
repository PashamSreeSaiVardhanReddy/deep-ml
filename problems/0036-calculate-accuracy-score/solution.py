import numpy as np

def accuracy_score(y_true, y_pred):
	y_true=np.asarray(y_true)
	y_pred=np.asarray(y_pred)
	score=np.mean(y_true==y_pred)
	return float(score)