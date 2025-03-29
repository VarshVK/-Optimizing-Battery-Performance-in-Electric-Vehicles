from django.db import models
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

#import cv2
import numpy as np
import pickle
#import pyreadstat
import json

import pandas as pd 



# Testing phase

rf = pickle.load(open(r"C:\Users\sanja\Desktop\CODE\FRONT END\RF.pkl", 'rb'))
dt = pickle.load(open(r"C:\Users\sanja\Desktop\CODE\FRONT END\xgb.pkl", 'rb'))


df = pd.read_csv(r'C:\Users\sanja\Desktop\CODE\FRONT END\test.csv')




# def predict(algo,row):
#     print(row)
# 	#print(x.columns)
#     test_data = df.iloc[row].values.reshape(1,-1)
#     print(test_data.shape)
# 	#print(test_data.columns)
#     if algo == 'dt':
# 	    y_pred = dt.predict(test_data)
#     elif algo == 'xgb':
# 	    y_pred = xgb.predict(test_data)
#     elif algo == 'etr':
# 	    y_pred = etr.predict(test_data)
#     else:
# 	    y_pred = rf.predict(test_data)
#     return y_pred

def predict(algo,row):
	#print(x.columns)
	test_data=df.iloc[row].values.reshape(1,-1)
	print(test_data.shape)
	#print(test_data.columns)
	if algo == 'dt':
		y_pred = dt.predict(test_data)
	else:
		y_pred = rf.predict(test_data)
	return y_pred
