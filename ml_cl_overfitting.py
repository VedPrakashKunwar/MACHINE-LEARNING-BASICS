# import module
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
############################ import data #################################
columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin", "car name"]
cars = pd.read_table("D:/Study/Dataquest/Data sets/auto-mpg.data", delim_whitespace=True, names = columns)

# looking into the data
'''
https://archive.ics.uci.edu/ml/datasets/Auto+MPG
1. mpg: continuous 
2. cylinders: multi-valued discrete 
3. displacement: continuous 
4. horsepower: continuous 
5. weight: continuous 
6. acceleration: continuous 
7. model year: multi-valued discrete 
8. origin: multi-valued discrete 
9. car name: string (unique for each instance)
'''
print(cars.info())

for col in columns:
    print(col)
    print(cars[col].unique())
    print('________________**********________________')
    
filtered_cars = cars[cars['horsepower'] != '?'].copy()
filtered_cars['horsepower'] = filtered_cars['horsepower'].astype('float')

"cylinders", "displacement", "horsepower", "weight", "acceleration"def train_and_test(cols):
    feature = cols
    target = 'mpg'
    model = LinearRegression()
    model.fit(filtered_cars[feature], filtered_cars[target])
    predict = model.predict(filtered_cars[feature])
    mse = mean_squared_error(predict, filtered_cars[target])
    variance = np.var(predict)
    return (mse, variance)
cyl_mse, cyl_var = train_and_test(['cylinders'])
weight_mse, weight_var = train_and_test(['weight'])
two_mse, two_var = train_and_test(['cylinders', 'displacement'])
three_mse, three_var = train_and_test(["cylinders", "displacement", "horsepower"])
four_mse, four_var = train_and_test(["cylinders", "displacement", "horsepower", "weight"])
five_mse, five_var = train_and_test(["cylinders", "displacement", "horsepower", "weight", "acceleration"])
six_mse, six_var = train_and_test(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year"])
seven_mse, seven_var = train_and_test(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin"])

'''
The multivariate regression models you trained got progressively better at reducing the amount of error.

A good way to detect if your model is overfitting is to compare the in-sample error and the out-of-sample error, or the training error with the test error. So far, we calculated the in sample error by testing the model over the same data it was trained on. To calculate the out-of-sample error, we need to test the data on a test set of data. We unfortunately don't have a separate test dataset and we'll instead use cross validation.

If a model's cross validation error (out-of-sample error) is much higher than the in sample error, then your data science senses should start to tingle. This is the first line of defense against overfitting and is a clear indicator that the trained model doesn't generalize well outside of the training set.
'''
for i in range(10):
    if i == 9:
        filtered_cars.loc[i*40:, 'fold'] = i
    else:
        filtered_cars.loc[i*40:(i+1)*40, 'fold'] = i


def train_and_cross_val(cols):
    np.random.seed(3)
    target = 'mpg'
    mse = []
    var = []
    for i in range(10):
        train_feature = filtered_cars.loc[filtered_cars['fold'] != i, cols]
        train_target = filtered_cars.loc[filtered_cars['fold']!=i, target]
        test_feature = filtered_cars.loc[filtered_cars['fold']==i, cols]
        test_target = filtered_cars.loc[filtered_cars['fold']==i, target]
        # apply model
        model = LinearRegression()
        model.fit(train_feature, train_target)
        predict = model.predict(test_feature)
        var.append(np.var(predict))
        mse.append(mean_squared_error(predict, test_target))
    return (np.mean(mse), np.mean(var))

two_mse, two_var = train_and_cross_val(['cylinders', 'displacement'])
three_mse, three_var = train_and_cross_val(["cylinders", "displacement", "horsepower"])
four_mse, four_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight"])
five_mse, five_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration"])
six_mse, six_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year"])
seven_mse, seven_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin"])



def train_and_cross_val2(cols):
    feature = filtered_cars[cols]
    target = filtered_cars['mpg']
    
    var = []
    mse = []
    # K-Fold instances
    kf = KFold(n_splits=10, shuffle=True, random_state=3)
    
    # iterating over each folds
    for train_index, test_index in kf.split(feature):
        X_train, X_test = feature.iloc[train_index], feature.iloc[test_index]
        y_train, y_test = target.iloc[train_index], target.iloc[test_index]
        lr = LinearRegression()
        lr.fit(X_train, y_train)
        predictions = lr.predict(X_test)
        var.append(np.var(predictions))
        mse.append(mean_squared_error(predictions, y_test))
        
    return (np.mean(mse), np.mean(var))

two_mse, two_var = train_and_cross_val2(['cylinders', 'displacement'])
three_mse, three_var = train_and_cross_val2(["cylinders", "displacement", "horsepower"])
four_mse, four_var = train_and_cross_val2(["cylinders", "displacement", "horsepower", "weight"])
five_mse, five_var = train_and_cross_val2(["cylinders", "displacement", "horsepower", "weight", "acceleration"])
six_mse, six_var = train_and_cross_val2(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year"])
seven_mse, seven_var = train_and_cross_val2(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin"])

plt.scatter([2,3,4,5,6,7], [two_mse, three_mse, four_mse, five_mse, six_mse, seven_mse], c='red')
plt.scatter([2,3,4,5,6,7], [two_var, three_var, four_var, five_var, six_var, seven_var], c='blue')
plt.show()