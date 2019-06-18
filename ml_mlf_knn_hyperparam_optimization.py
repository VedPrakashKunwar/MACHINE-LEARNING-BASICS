# import module
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# import data
train_df = pd.read_csv("D:/Study/Dataquest/Data sets/dc_airbnb_train.csv")
test_df = pd.read_csv("D:/Study/Dataquest/Data sets/dc_airbnb_test.csv")

# checking the params for k = 1 to 5
hyper_params = [1, 2, 3, 4, 5]
mse_values = []
features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
for i in hyper_params:
    knn = KNeighborsRegressor(algorithm='brute', n_neighbors=i)
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse_values.append(mean_squared_error(test_df['price'], predictions))
    
# checking the params for k = 1 to 20
hyper_params_20 = list(range(1,50)) # or [x for x in range(1,21)]
mse_values_20 = []
features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
for i in hyper_params_20:
    knn = KNeighborsRegressor(algorithm='brute', n_neighbors=i)
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse_values_20.append(mean_squared_error(test_df['price'], predictions))

# plotting the mse value against the k value
plt.scatter(hyper_params_20, mse_values_20)
plt.show()

# using all column in the model
hyper_params = [x for x in range(1,21)]
mse_values_all = list()
features_all = train_df.columns.tolist()
features_all.remove('price')

for i in hyper_params:
    knn = KNeighborsRegressor(algorithm='brute', n_neighbors=i)
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse_values_all.append(mean_squared_error(test_df['price'], predictions))
    

plt.scatter(hyper_params, mse_values_all)
plt.show()
