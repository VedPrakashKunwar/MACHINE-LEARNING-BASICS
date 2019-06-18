# import module
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
############################ import data #################################
df = pd.read_table("D:/Study/Dataquest/Data sets/imports-85.data", sep=',', header=None)

# looking into the data
print(df.info()) # no null value
col = [0, 1, 5, 9, 10, 11, 12, 13, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25]
df_copy = df[col].copy()
# looking into column 1 aka
df_copy[1].value_counts() # too many ? value so removing the column
df_copy.drop(1, axis = 1, inplace=True)
col.remove(1)

# looking into col 5
df_copy[5].value_counts()
df_copy.loc[df_copy[5] == 'four', 5] = 4
df_copy.loc[df_copy[5] == 'two', 5] = 2
df_copy = df_copy.loc[df_copy[5] != '?']
df_copy[5] = df_copy[5].astype(int)

# looking into column 9
df_copy[9].value_counts()
# looking into column 15
df_copy[15].value_counts()
df_copy.loc[df_copy[15] == 'four', 15] = 4
df_copy.loc[df_copy[15] == 'two', 15] = 2
df_copy.loc[df_copy[15] == 'six', 15] = 6
df_copy.loc[df_copy[15] == 'five', 15] = 5
df_copy.loc[df_copy[15] == 'eight', 15] = 8
df_copy.loc[df_copy[15] == 'twelve', 15] = 12
df_copy.loc[df_copy[15] == 'three', 15] = 3
df_copy[15] = df_copy[15].astype(int)

# looking into column 18
df_copy[18].value_counts()
df_copy = df_copy.loc[df_copy[18] != '?']
df_copy[18] = df_copy[18].astype(float)

# looking into column 19
df_copy[19].value_counts()
df_copy[19] = df_copy[19].astype(float)

# looking into column 21
df_copy[21].value_counts()
df_copy = df_copy.loc[df_copy[21] != '?']
df_copy[21] = df_copy[21].astype(int)

# verify the data once
df_copy.info()

# looking into column 22
df_copy[22].value_counts()
df_copy[22] = df_copy[22].astype(int)

# looking into column 25
df_copy[25].value_counts()
df_copy = df_copy.loc[df_copy[25] != '?']
df_copy[25] = df_copy[25].astype(int)

# verify the data once
df_copy.info()

####################################### start prediction ########################
shuffled_index = np.random.permutation(df_copy.index)
df_copy = df_copy.reindex(shuffled_index)
train_df = df_copy[0:140]
test_df = df_copy[140:]
feature = col
#feature.remove(25)
knn = KNeighborsRegressor(n_neighbors=5, algorithm='auto')
knn.fit(train_df[feature], train_df[25])
predictions = knn.predict(test_df[feature])
rmse_5 = mean_squared_error(test_df[25], predictions)**0.5
rmses = []
for i in list(range(1,20)):
    knn = KNeighborsRegressor(n_neighbors=i, algorithm='auto')
    knn.fit(train_df[feature], train_df[25])
    predictions = knn.predict(test_df[feature])
    rmse = mean_squared_error(test_df[25], predictions)**0.5
    rmses.append(rmse)
    
# plot the chart
plt.scatter(list(range(1, 20)), rmses)
plt.show()
# so we find that k = 12 
knn = KNeighborsRegressor(n_neighbors=12, algorithm='auto')
knn.fit(train_df[feature], train_df[25])
predictions = knn.predict(test_df[feature])
rmse = mean_squared_error(test_df[25], predictions)**0.5

test_df.loc[:, 'predicted_price'] = predictions

########################## normalise the data ###################################
normalized_listings = (df_copy-df_copy.mean())/df_copy.std()
normalized_listings[25] = df_copy[25]
shuffled_index = np.random.permutation(normalized_listings.index)
normalized_listings = normalized_listings.reindex(shuffled_index)
train_df = normalized_listings[0:140]
test_df = normalized_listings[140:]

feature = col
feature.remove(25)
knn = KNeighborsRegressor(n_neighbors=5, algorithm='auto')
knn.fit(train_df[feature], train_df[25])
predictions = knn.predict(test_df[feature])
rmse_5 = mean_squared_error(test_df[25], predictions)**0.5
rmses_norm = []
for i in list(range(1,20)):
    knn = KNeighborsRegressor(n_neighbors=i, algorithm='auto')
    knn.fit(train_df[feature], train_df[25])
    predictions = knn.predict(test_df[feature])
    rmse_norm = mean_squared_error(test_df[25], predictions)**0.5
    rmses_norm.append(rmse_norm)
    
# plot the chart
plt.scatter(list(range(1, 20)), rmses_norm)
plt.show()
# so we find that k = 10
knn = KNeighborsRegressor(n_neighbors=12, algorithm='auto')
knn.fit(train_df[feature], train_df[25])
predictions = knn.predict(test_df[feature])
rmse = mean_squared_error(test_df[25], predictions)**0.5

test_df.loc[:, 'predicted_price'] = predictions