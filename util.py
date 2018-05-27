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

	cities_algarve = ['Faro','Silves','Lagos','Olhão','Albufeira','Lagoa','Portimão','Loulé','Monchique','Tavira']

	if row['Hospital active'] == 0:
		return 0 
	else:
		city = row['City']
		day_of_week = row['Date'].weekday_name
		if day_of_week == 'Sunday':
			return ceil(df_quantil_Sun.loc[(city,day_of_week)]/15*15)
		elif day_of_week == 'Monday':
			if city in cities_algarve:
				return ceil(0.4*df_quantil_Mon.loc[(city,day_of_week)]/15)
			else:
				return ceil(0.9145*df_quantil_Mon.loc[(city,day_of_week)]/15)
		elif day_of_week == 'Tuesday':
			if city in cities_algarve:
				return ceil(0.50*df_quantil_Tue.loc[(city,day_of_week)]/15)
			else:
				return ceil(df_quantil_Tue.loc[(city,day_of_week)]/15)
		elif day_of_week == 'Wednesday':
			if city in cities_algarve:
				return ceil(df_quantil_Wen.loc[(city,day_of_week)]/15)
			else:
				return ceil(df_quantil_Wen.loc[(city,day_of_week)]/15)

def get_hollidays():
    return pd.read_csv('data/cities_with_student_holidays.txt', header=None, delimiter="'")[1].tolist()

def get_test_holliday_df(df_):
    df_new = df_.copy()
    hollidays = get_hollidays()
    df_new["isHolliday"] = df_new["City"].isin(hollidays).astype(int)
    return df_new
