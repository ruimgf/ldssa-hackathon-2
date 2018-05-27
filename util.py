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

def get_quantil_pred(row,df_quantil_Sun,df_quantil_Mon,df_quantil_Tue,df_quantil_Wen):
	if row['Hospital active'] == 0:
		return 0 
	else:
		city = row['City']
		day_of_week = row['Date'].weekday_name
		if day_of_week == 'Sunday':
			return ceil(df_quantil_Sun.loc[(city,day_of_week)]/15)
		elif day_of_week == 'Monday':
			return ceil(df_quantil_Mon.loc[(city,day_of_week)]/15)
		elif day_of_week == 'Tuesday':
			return ceil(df_quantil_Tue.loc[(city,day_of_week)]/15)
		elif day_of_week == 'Wednesday':
			return ceil(df_quantil_Wen.loc[(city,day_of_week)]/15)
