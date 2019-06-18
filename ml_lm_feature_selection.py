# import module
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
############################ import data #################################
data = pd.read_table("D:/Study/Dataquest/Data sets/AmesHousing.txt", sep='\t')

# divide into train and test set
train = data[0:1460]
test = data[1460:]
print(data.info())
# only taking numerical value in the datasets
numerical_train = train.select_dtypes(include=['int64', 'float64'])
numerical_train = numerical_train.drop(['PID', 'Year Built', 'Year Remod/Add', 'Garage Yr Blt', 'Mo Sold', 'Yr Sold'], axis=1)
null_series = numerical_train.isnull().sum()
full_cols_series = null_series[null_series == 0]
print(full_cols_series)
train_subset = train[full_cols_series.index]
sorted_corrs = train_subset.corr().loc[:, 'SalePrice'].abs().sort_values()

# generating correlation matrix heatmap
# we are taking values with more that 0.3 correlation
# 0.3 is choosed randomnly
strong_corrs = sorted_corrs[sorted_corrs > 0.3]
corrmat = train_subset[strong_corrs.index].corr()
sns.heatmap(corrmat)
# looking at heatmap we see two variable pair strongly correlated
# Gr Liv Area and TotRms AbvGrd
# Garage Area and Garage Cars
# Because Gr Liv Area and Garage Area are continuous variables that capture more nuance, 
# let's drop the TotRms AbvGrd and Garage Cars.
final_corr_cols = strong_corrs.drop(['Garage Cars', 'TotRms AbvGrd'])
clean_test = train_subset[final_corr_cols.index]
final_corr_cols = final_corr_cols.index
lr = LinearRegression()
lr.fit(train[final_corr_cols], train['SalePrice'])
target = 'SalePrice'
train_predictions = lr.predict(train[final_corr_cols])
test_predictions = lr.predict(clean_test[final_corr_cols])

train_mse = mean_squared_error(train_predictions, train[target])
test_mse = mean_squared_error(test_predictions, clean_test[target])

train_rmse = np.sqrt(train_mse)
test_rmse = np.sqrt(test_mse)

# doing rescaling in the data
# rescaling = (x - min(x))/(max(x) - min(x))
unit_train = (train[final_corr_cols] - train[final_corr_cols].min())/(train[final_corr_cols].max() - train[final_corr_cols].min())
sorted_vars = unit_train.var().sort_values()
# build model on correlation 0.15
strong_corrs_2 = sorted_corrs[sorted_corrs > 0.15]
corrmat_2 = train_subset[strong_corrs_2.index].corr()
sns.heatmap(corrmat_2)
final_corr_cols_2 = strong_corrs.drop(['Garage Cars', 'TotRms AbvGrd', 'Open Porch SF'])
final_corr_cols_2 = final_corr_cols_2.index

lr = LinearRegression()
lr.fit(train[final_corr_cols_2], train['SalePrice'])
target = 'SalePrice'
train_predictions_2 = lr.predict(train[final_corr_cols_2])
test_predictions_2 = lr.predict(clean_test[final_corr_cols_2])

train_mse = mean_squared_error(train_predictions_2, train[target])**0.5
test_mse = mean_squared_error(test_predictions_2, clean_test[target])**0.5

