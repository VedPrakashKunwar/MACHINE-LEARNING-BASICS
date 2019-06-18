# import module
from numpy.random import randint, seed
from numpy import std, var
import pandas as pd
import matplotlib.pyplot as plt
import math
houses = pd.read_table('D:/Study/Dataquest/Data Sets/AmesHousing_1.txt')

# variablitily (range)
def arr_range(array):
    # assing inf to min and -inf to max
    min = math.inf
    max = -1*math.inf
    for value in array:
        if value > max:
            max = value
        if value < min:
            min = value
    return max-min


range_by_year = {}
years = houses['Yr Sold'].unique()
for year in years:
    range_by_year[year] = arr_range(houses.loc[houses['Yr Sold']==year, 'SalePrice'])
    
# above method for variability in not good as it takes only 2 value into account.

# average distance
def avg_dist(array):
    mean = sum(array)/len(array)
    dist = []
    for value in array:
        dist.append(value-mean)
    return sum(dist)/len(dist)
 
C = [1,1,1,1,1,1,1,1,1,21]
avg_distance = avg_dist(C) 

# absolute average distance
def abs_avg_dist(array):
    mean = sum(array)/len(array)
    dist = []
    for value in array:
        dist.append(abs(value-mean))
    return sum(dist)/len(dist)
mad = abs_avg_dist(C)

# mean squared distance
def mean_sqr_dist(array):
    mean = sum(array)/len(array)
    dist = []
    for value in array:
        dist.append((value-mean)**2)
    return sum(dist)/len(dist)
variance_C = mean_sqr_dist(C)

# standard deviation
def std_dev(array):
    mean = sum(array)/len(array)
    dist = []
    for value in array:
        dist.append((value-mean)**2)
    return math.sqrt(sum(dist)/len(dist))
standard_deviation_C = std_dev(C)

# generate histogram for sale price
mean = houses['SalePrice'].mean()
standard_deviation = std_dev(houses['SalePrice'])
houses['SalePrice'].plot.hist()
plt.axvline(mean-standard_deviation, color = 'red', label='below')
plt.axvline(mean+standard_deviation, color='blue', label='above')
plt.axvline(mean, color='green', label='mean')
plt.legend()

# sample standard deviation
sample = houses.sample(100, random_state = 1)
pandas_stdev = sample['SalePrice'].std(ddof=1)
numpy_stdev = std(sample['SalePrice'], ddof=1)
equal_stdevs = pandas_stdev==numpy_stdev
pandas_var = sample['SalePrice'].var(ddof=1)
numpy_var = var(sample['SalePrice'], ddof=1)
equal_vars = pandas_var==numpy_var

# sample variance
population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]
variances = []
std_dev = []
for i in samples:
    variances.append(var(i))
    std_dev.append(std(i))
      
mean_var = sum(variances)/len(variances)
mean_std_dev = sum(std_dev)/len(std_dev)

