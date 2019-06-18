# import module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand
from numpy import mean
from scipy.stats import chisquare
from scipy.stats import chi2_contingency
income = pd.read_table('D:/Study/Dataquest/Data Sets/income.csv', sep=',')

'''
In the single category chi-squared test, we find expected values from other data sets, 
and then compare with our own observed values. In a multiple category chi-squared test, 
we calculate expected values across our whole dataset.
'''

'''
20.5% of Males in the whole data set earn >50k in income.
33% of the whole dataset is Female
75.9% of the whole dataset earns <=50k.
We can use our total proportions to calculate expected values. 24.1% of all people 
in income earn >50k, and 33% of all people in income are Female, so we'd expect the 
proportion of people who are female and earn >50k to be 0.241 * 0.33, which is 0.07953. 
We have this expectation based on the proportions of Females and >50k earners across the 
whole dataset. Instead, we see that the observed proportion is 0.036, which indicates 
that there may be some correlation between the sex and high_income columns.


We can convert our expected proportion to an expected value by multiplying by 32561, 
the total number of rows in the data set, which gives us 32561 * 0.07953, or 2589.6.
'''

# finding expected propotion
males_over50k = 32561*0.67*0.241
males_under50k = 32561*0.67*0.759
females_over50k = 32561*0.33*0.241
females_under50k = 32561*0.33*0.759

'''
Now that we have our expected values, we can calculate the chi-squared value by using 
the same principle from the previous mission. Here are the steps:

Subtract the expected value from the observed value.
Square the difference.
Divide the squared difference by the expected value.
Repeat for all the observed and expected values and add up the values.
'''
table = pd.crosstab(income["sex"], [income["high_income"]])
print(table)

table1 = pd.crosstab(income['sex'], [income['race']])
print(table1)

observed = np.array([[119, 346, 1555, 109, 8642], [192, 693, 1569, 162, 19174]])
chisq_value, pvalue_gender_race, df, expected = chi2_contingency(observed)