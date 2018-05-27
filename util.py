import numpy as np
from math import ceil
def error_function(n_patients,n_doctors):
	error = (n_patients - n_doctors * 15)
	return np.sum(np.maximum(np.zeros(error.shape),error))

def get_simple_pred(row,df_mean):
	if row['Hospital active'] == 0:
		return 0 
	else:
		city = row['City']
		return ceil(df_mean.loc[city]/15*0.84)