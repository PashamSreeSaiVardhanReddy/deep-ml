import numpy as np
def feature_scaling(data):
	data=np.asarray(data)
	x_min=np.min(data,axis=0,keepdims=True)
	x_max=np.max(data,axis=0,keepdims=True)
	denom=x_max-x_min
	denom[denom==0]=1.0
	feature=(data-x_min)/denom
	stdn=np.std(data,axis=0)
	m=np.mean(data,axis=0)
	scaling=(data-m)/stdn
	return scaling.tolist(),feature.tolist()
