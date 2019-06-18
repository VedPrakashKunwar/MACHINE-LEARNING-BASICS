# import  module
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
############################ import data #################################
cars = pd.read_table("D:/Study/Dataquest/Data sets/auto.csv", sep=',')
# origin is the output data
unique_origins = cars['origin'].unique()
cylinders = pd.get_dummies(cars['cylinders'], prefix='cyl')
cars = pd.concat([cars, cylinders], axis = 1)
dummy_years = pd.get_dummies(cars['year'], prefix='year')
cars = pd.concat([cars, dummy_years], axis = 1)
cars = cars.drop("year", axis=1)
cars = cars.drop("cylinders", axis=1)
print(cars.head())
# When we have 3 or more categories, we call the problem a multiclass classification problem.
# The one-versus-all method is a technique where we choose a single category as the Positive case and group the rest of the categories as the False case. We're essentially splitting the problem into multiple binary classification problems. For each observation, the model will then output the probability of belonging to each category.

# shuffel the dataset and divide into train and test sets
shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]

train = shuffled_cars[0:274]
test = shuffled_cars[274:]

# In the one-vs-all approach, we're essentially converting an n-class (in our case n is 3) classification problem into n binary classification problems. For our case, we'll need to train 3 models:

#A model where all cars built in North America are considered Positive (1) and those built in Europe and Asia are considered Negative (0).
#A model where all cars built in Europe are considered Positive (1) and those built in North America and Asia are considered Negative (0).
#A model where all cars built in Asia are labeled Positive (1) and those built in North America and Europe are considered Negative (0).


models = {}
testing_probs = pd.DataFrame(columns=unique_origins)  
# features = [c for c in train.columns if c.startswith("cyl") or c.startswith("year")]
for origin in unique_origins:
    model = LogisticRegression()
    
    X_train = train.loc[:, 'cyl_3':'year_82']
    y_train = train['origin']==origin
    
    model.fit(X_train, y_train)
    models[origin] = model
    probab = model.predict_proba(test.loc[:, 'cyl_3':'year_82'])[:,1]
    testing_probs[origin] = probab
    
# getting the value with maximum probability accross the columns
predicted_origins = testing_probs.idxmax(axis = 1)