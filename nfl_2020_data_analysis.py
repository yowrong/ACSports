# import data summary table
# perform statistical data analysis

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("nfl_2020_data_summary.csv")
print(data.head())

X = data.loc[:, 'H-A_SRS'].values.reshape(-1, 1)  # values converts it into a numpy array
Y = data.loc[:, 'YPP_Margin'].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column

model = LinearRegression()  # create object for the class
model.fit(X, Y)  # perform linear regression
Y_pred = model.predict(X)  # make predictions

r_sq = model.score(X, Y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print('predicted response:', Y_pred, sep='\n')