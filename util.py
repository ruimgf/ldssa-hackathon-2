import numpy as np

def error_function(n_patients,n_doctors):
	error = (n_patients - n_doctors * 15)
	return np.sum(np.maximum(np.zeros(error.shape),error))

def get_simple_pred(row):