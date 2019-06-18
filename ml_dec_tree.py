# import module
import pandas as pd
import math
import numpy as np
############################ import data #################################
income = pd.read_table("D:/Study/Dataquest/Data sets/income1.csv", sep=',')

# looking into data
print(income.head(5))
print(income.info())
print(income.isnull().sum()) # no missing value

cols = income.columns
for col in cols:
    print('_______________________________*** ', col, ' ***_________________________________')
    print()
    print(income[col].unique())
    print()

# all object is having the space in the starting 
text_cols = income.select_dtypes(include='object').columns
for col in text_cols:
    income[col] = income[col].str.lstrip()

# =============================================================================
# # looking into occupation and workclass and income
# zz = pd.crosstab(income.occupation, [income.high_income, income.workclass])
# income.loc[(income['occupation']=='?') & (income['workclass']=='?'), 'occupation'] = 'No Job' 
# income.loc[(income['occupation']=='?') & (income['workclass']=='?'), 'workclass'] = 'No Job' 
# =============================================================================

# dropping row with ? value
income = income.loc[income['occupation'] != '?', :]

# converting object column into categorical variable
text_cols = income.select_dtypes(include='object').columns
for col in text_cols:
    category = pd.Categorical(income[col])
    income[col] = category.codes
   
cols = income.columns
for col in cols:
    print('_______________________________*** ', col, ' ***_________________________________')
    print()
    print(income[col].unique())
    print()
    
# splitting the data based on workclass
private_incomes = income[income['workclass']==4].copy()
public_incomes = income[income['workclass']!=4].copy()
'''
The nodes at the bottom of the tree, where we decide to stop splitting, are called terminal nodes, or leaves. When we do our splits, we aren't doing them randomly; we have an objective. Our goal is to ensure that we can make a prediction on future data. In order to do this, all rows in each leaf must have only one value for our target column.

When we split, we'll try to separate as many 0s from 1s in the high_income column as we can. In order to do this, we need a metric for how "together" the different values in the high_income column are.

Data scientists commonly use a metric called entropy for this purpose. Entropy refers to disorder. The more "mixed together" 1s and 0s are, the higher the entropy. A data set consisting entirely of 1s in the high_income column would have low entropy.
'''

# calculating the entropy of high income
income['high_income'].value_counts()
prob_high = income[income['high_income']==1].shape[0]/income.shape[0]
high_income =  -(prob_high*math.log(prob_high, 2) + (1-prob_high)*math.log(1-prob_high, 2))

# calculating the entropy for age
# median of age
import numpy

def calc_entropy(column):
    """
    Calculate entropy given a pandas series, list, or numpy array.
    """
    # Compute the counts of each unique value in the column
    counts = numpy.bincount(column)
    # Divide by the total column length to get a probability
    probabilities = counts / len(column)
    
    # Initialize the entropy to 0
    entropy = 0
    # Loop through the probabilities, and add each one to the total entropy
    for prob in probabilities:
        if prob > 0:
            entropy += prob * math.log(prob, 2)
    
    return -entropy

# Verify that our function matches our answer from earlier
entropy = calc_entropy([1,1,0,0,1])
print(entropy)

information_gain = entropy - ((.8 * calc_entropy([1,1,0,0])) + (.2 * calc_entropy([1])))
print(information_gain)
income_entropy = calc_entropy(income["high_income"])

median_age = income["age"].median()

left_split = income[income["age"] <= median_age]
right_split = income[income["age"] > median_age]

age_information_gain = income_entropy - ((left_split.shape[0] / income.shape[0]) * calc_entropy(left_split["high_income"]) + ((right_split.shape[0] / income.shape[0]) * calc_entropy(right_split["high_income"])))