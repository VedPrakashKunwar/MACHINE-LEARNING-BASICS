# import module
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
############################ import data #################################
data = pd.read_table("D:/Study/Dataquest/Data sets/AmesHousing.txt", sep='\t')

# divide into train and test set
train = data[0:1460]
test = data[1460:]
data.info()
target = 'SalePrice'

# finding the best variable
fig = plt.figure(figsize=(7,15))

ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

train.plot(x="Garage Area", y="SalePrice", ax=ax1, kind="scatter")
train.plot(x="Gr Liv Area", y="SalePrice", ax=ax2, kind="scatter")
train.plot(x="Overall Cond", y="SalePrice", ax=ax3, kind="scatter")

plt.show()
# conferming with the correlation
print(train[['Garage Area', 'Gr Liv Area', 'Overall Cond', 'SalePrice']].corr())

# make model
feature = ['Gr Liv Area']
target = 'SalePrice'
lm = LinearRegression()
lm.fit(train[feature], train[target])
coeff = lm.coef_
intercept = lm.intercept_
prediction_train = lm.predict(train[feature])
prediction_test = lm.predict(test[feature])
train_rmse = mean_squared_error(train[target], prediction_train)**0.5
test_rmse = mean_squared_error(test[target], prediction_test)**0.5

# make model with two feature
feature = ['Gr Liv Area', 'Overall Cond']
target = 'SalePrice'
lm = LinearRegression()
lm.fit(train[feature], train[target])
prediction_train_2 = lm.predict(train[feature])
prediction_test_2 = lm.predict(test[feature])
train_rmse_2 = mean_squared_error(train[target], prediction_train_2)**0.5
test_rmse_2 = mean_squared_error(test[target], prediction_test_2)**0.5

