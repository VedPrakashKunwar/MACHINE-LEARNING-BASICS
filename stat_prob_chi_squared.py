# import module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand
from numpy import mean
from scipy.stats import chisquare
income = pd.read_table('D:/Study/Dataquest/Data Sets/income.csv', sep=',')

print(income['sex'].value_counts())
'''
The entire dataset has 32561 rows, and is a sample of the full Census. Of the rows, 
10771 are Female, and 21790 are Male. These numbers look a bit off, because the full 
Census shows that the US is about 50% Male and 50% Female. So our expected values for 
number of Males and Females would be 16280.5 each

We know that something looks off, but we don't quite know how to quantify how different 
the observed and expected values are. We also don't have any way to determine if there's 
a statistically significant difference between the two groups, and if we need to  
investigate further.

One way that we can determine the differences between observed and expected values is to 
compute simple proportional differences.

Let's say an expected value is 1000, and the observed value is 1100. We can compute the 
proportional difference with:
    =(observed-expected)/expected

We can get one step closer to this by squaring the top term in our difference formula:
    =((observed-expected)**2)/expected

We can calculate , the chi-squared value, by adding up all of the squared differences 
between observed and expected values.
'''
# propotional difference
female_diff = (10771-16280.5)/16280.5
male_diff = (21790-16280.5)/16280.5

# chi-squared
female_diff = (10771-16280.5)**2/16280.5
male_diff = (21790-16280.5)**2/16280.5
gender_chisq = female_diff+male_diff

'''
We can generate a chi-squared sampling distribution using our expected probabilities. 
If we repeatedly generate random samples that contain 32561 samples, and graph the 
chi-squared value of each sample, we'll be able to generate a distribution. Here's a 
rough algorithm:

Randomly generate 32561 numbers that range from 0-1.
Based on the expected probabilities, assign Male or Female to each number.
Compute the observed frequences of Male and Female.
Compute the chi-squared value and save it.
Repeat several times.
Create a histogram of all the chi-squared values.


By comparing our chi-squared value to the distribution, and seeing what percentage of 
the distribution is greater than our value, we'll get a p-value. For instance, if 5% of 
the values in the distribution are greater than our chi-squared value, 
the p-value is .05.
'''

# let's begin
chi_squared_values = []
# zero one generator
def zero_one(x):
    if x >= 0.5:
        return 1
    else:
        return 0
    
    
for i in range(1000):
    # genderate randomm no
    random_val = rand.random(32561,)
    
    # generate 0's and 1's
    random_value = [zero_one(x) for x in random_val]
    
    # count 0 and 1 in abover vector
    male = 0 # male = 0
    female = 0 # female = 1
    for i in random_value:
        if i == 0:
            male += 1
        else:
            female += 1
            
    # call che squared
    chi_squared_value = ((female-32561/2)**2)/(32561/2) + ((male-32561/2)**2)/(32561/2)
    chi_squared_values.append(chi_squared_value)
    
plt.hist(chi_squared_values)
plt.show()


# above can be done following way
for i in range(1000):
    sequence = random((32561,))
    sequence[sequence < .5] = 0
    sequence[sequence >= .5] = 1
    male_count = len(sequence[sequence == 0])
    female_count = len(sequence[sequence == 1])
    male_diff = (male_count - 16280.5) ** 2 / 16280.5
    female_diff = (female_count - 16280.5) ** 2 / 16280.5
    chi_squared = male_diff + female_diff
    chi_squared_values.append(chi_squared)

plt.hist(chi_squared_values)


''' 
Now that we have a chi-squared sampling distribution, we can compare the 
chi-squared value we calculated for our data to it to see if our result is statistically
significant. The chi-squared value we calculated was 3728.95. The highest value in 
the chi-squared sampling distribution was about 12. This means that our chi-squared 
value is higher than 100% of all the values in the sampling distribution, so we get a 
p-value of 0. This means that there is a 0% chance that we could get such a result 
randomly.

As sample size changes, the chi-squared value changes proportionally.

Chi-squared values increase as sample size increases, but the chance of getting a 
high chi-squared value decreases as the sample gets larger.
 '''
 
'''
Rather than constructing another chi-squared sampling distribution for 4 degrees of 
freedom, we can use a function from the SciPy library to do it more quickly.

The scipy.stats.chisquare function takes in an array of observed frequences, 
and an array of expected frequencies, and returns a tuple containing both the 
chi-squared value and the matching p-value that we can use to check for statistical 
significance.
'''

observed = np.array([5, 10, 15])
expected = np.array([7, 11, 12])
race_pvalue = chisquare(observed, expected)