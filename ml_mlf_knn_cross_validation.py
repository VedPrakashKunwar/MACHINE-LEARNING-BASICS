# import module
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold, cross_val_score

########################## read data ##########################################
dc_listings = pd.read_csv("D:/Study/Dataquest/Data sets/dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

####################### make train and test sets ##############################
shuffled_index = np.random.permutation(dc_listings.index)
dc_listings = dc_listings.reindex(shuffled_index)
split_one = dc_listings[0:1862]
split_two = dc_listings[1862:]

'''
we are working on the holdout validation method. In this the dataset is divided into two equal part
and make both part as train and test and find the mse in each case and get the mean mse
'''

train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one
feature = ['accommodates']
# training the first model
knn = KNeighborsRegressor(algorithm='auto', 
                          n_neighbors=5)
knn.fit(train_one[feature], train_one['price'])
predictions = knn.predict(test_one[feature])
iteration_one_mse = mean_squared_error(predictions, test_one['price'])**0.5

# training the second model
knn = KNeighborsRegressor(algorithm='auto', 
                          n_neighbors=5)
knn.fit(train_two[feature], train_two['price'])
predictions = knn.predict(test_two[feature])
iteration_one_mse = mean_squared_error(predictions, test_one['price'])**0.5

avg_rmse = mean()

'''
While holdout validation is better than train/test validation because the model isn't repeatedly 
biased towards a specific subset of the data, both models that are trained only use half the 
available data. K-fold cross validation, on the other hand, takes advantage of a larger 
proportion of the data during training while still rotating through different subsets of the 
data to avoid the issues of train/test validation.

Here's the algorithm from k-fold cross validation:

    splitting the full dataset into k equal length partitions.
    selecting k-1 partitions as the training set and
    selecting the remaining partition as the test set
    training the model on the training set.
    using the trained model to predict labels on the test fold.
    computing the test fold's error metric.
    repeating all of the above steps k-1 times, until each partition has been used as the 
    test set for an iteration.
    calculating the mean of the k error values.
    
Holdout validation is essentially a version of k-fold cross validation when k is equal to 2. 
Generally, 5 or 10 folds is used for k-fold cross-validation.
'''
# we are dividing the dataset into five fold
# we will add the the fold column in the dataset which will tell which folds the data belongs to
dc_listings.loc[0:745,'fold'] = 1
dc_listings.loc[745:1490,'fold'] = 2
dc_listings.loc[1490:2234,'fold'] = 3
dc_listings.loc[2234:2978,'fold'] = 4
dc_listings.loc[2978:3723,'fold'] = 5
# checking the fold has equal no of value
print(dc_listings['fold'].value_counts())
print(dc_listings['fold'].isnull().sum())

# making fold 1 as test test and fold 2-5 as train set
train_df = dc_listings.loc[dc_listings['fold'] > 1]
test_df = dc_listings.loc[dc_listings['fold'] == 1]
feature = ['accommodates']
knn = KNeighborsRegressor(algorithm='auto', n_neighbors=5)
#knn.fit(train_two[feature], train_two['price'])
knn.fit(train_df[feature], train_df['price'])
predictions = knn.predict(test_df[feature])
iteration_one_rmse = mean_squared_error(test_df['price'], predictions)**0.5


# writing function 
def train_and_validate(df, fold):
    rmse = []
    for i in fold:
        train_df = dc_listings.loc[dc_listings['fold'] != i]
        test_df = dc_listings.loc[dc_listings['fold'] == i]
        feature = ['accommodates']
        knn = KNeighborsRegressor(algorithm='auto', n_neighbors=5)
        knn.fit(train_df[feature], train_df['price'])
        predictions = knn.predict(test_df[feature])
        rmse.append(mean_squared_error(test_df['price'], predictions)**0.5)
    return rmse
fold = [x for x in range(1, 6)]
rmses = train_and_validate(dc_listings, fold)
avg_rmse = np.mean(rmses)

# using kfold, and cross_val_score
kf = KFold(n_splits=5, shuffle=True, random_state=1)
knn = KNeighborsRegressor(n_neighbors=5, algorithm='auto')
mses = cross_val_score(knn, dc_listings[["accommodates"]], 
                dc_listings["price"], 
                scoring="neg_mean_squared_error", 
                cv=kf
                )
rmses = np.sqrt(np.absolute(mses))
avg_rmse = np.mean(rmses)

# for different kfold
num_folds = [3, 5, 7, 9, 10, 11, 13, 15, 17, 19, 21, 23]

for fold in num_folds:
    kf = KFold(fold, shuffle=True, random_state=1)
    model = KNeighborsRegressor()
    mses = cross_val_score(model, dc_listings[["accommodates"]], dc_listings["price"], scoring="neg_mean_squared_error", cv=kf)
    rmses = np.sqrt(np.absolute(mses))
    avg_rmse = np.mean(rmses)
    std_rmse = np.std(rmses)
    print(str(fold), "folds: ", "avg RMSE: ", str(avg_rmse), "std RMSE: ", str(std_rmse))