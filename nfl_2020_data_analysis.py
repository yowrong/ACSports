# import data summary table
# perform statistical data analysis

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("nfl_2020_data_summary.csv")
print(data.head())

X1 = data.loc[:, 'YPP_Margin'].values.reshape(-1, 1)
X2 = data.loc[:, 'H-A_SRS'].values.reshape(-1, 1)  # values converts it into a numpy array
Y = data.loc[:, 'H-A_Margin'].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column

model = LinearRegression()  # create object for the class
model.fit(X1, Y)  # perform linear regression
Y_pred = model.predict(X1)  # make predictions

r_sq = model.score(X1, Y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
# print('predicted response:', Y_pred, sep='\n')


x1 = X1.flatten()
x2 = X2.flatten()
y = Y.flatten()
# print('x:', x, sep='\n')


# plot points and fit line with matplotlib
# plt.scatter(X, Y)
# b = model.coef_
# a = model.intercept_
# yfit = [a + b * xi for xi in X]
# plt.plot(X, yfit)
# plt.show()

plotA = plt
plotB = plt

# plot points and fit line with numpy
plotA.plot(x1, y, 'o')
m, b = np.polyfit(x1, y, 1)
plotA.plot(x1, m*x1 + b)
plotA.scatter(x1, y)
plotA.title("NFL Stat vs Score Correlation")
plotA.xlabel("Yards Per Play Margin")
plotA.ylabel("Home - Away Score Margin")
plotA.show()

plotB.plot(x2, y, 'o')
m, b = np.polyfit(x2, y, 1)
plotB.plot(x2, m*x2 + b)
plotB.scatter(x2, y)
plotB.title("NFL Stat vs Score Correlation")
plotB.xlabel("Home - Away SRS Margin")
plotB.ylabel("Home - Away Score Margin")
plotB.show()


