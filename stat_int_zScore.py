# import module
from numpy.random import randint, seed
from numpy import std, var
import pandas as pd
import matplotlib.pyplot as plt
import math
houses = pd.read_table('D:/Study/Dataquest/Data Sets/AmesHousing_1.txt')

houses['SalePrice'].plot.kde(xlim = (houses['SalePrice'].min(), houses['SalePrice'].max()) )
plt.axvline(houses['SalePrice'].mean(), color = 'green', label = 'mean')
plt.axvline(houses['SalePrice'].std(ddof=0)+houses['SalePrice'].mean(), color = 'red', label = 'Standard deviation')
plt.axvline(222000, label = '222000', color = 'orange')
plt.legend()
# how many standard deviation away is 220000
st_devs_away = (220000-houses['SalePrice'].mean())/houses['SalePrice'].std(ddof=0)

''' Z-Score
z = (value-mean)/standard deviation
The value representing the number of standard deviations away from the mean is commonly 
known as the standard score
'''
min_val = houses['SalePrice'].min()
mean_val = houses['SalePrice'].mean()
max_val = houses['SalePrice'].max()

def z_score(val, arr):
    arr_mean = sum(arr)/len(arr)
    arr_std = std(arr)
    return (val-arr_mean)/arr_std

min_z = z_score(min_val, houses['SalePrice'])
max_z = z_score(max_val, houses['SalePrice'])
mean_z = z_score(mean_val, houses['SalePrice'])

# z-score for 200,000 area wise (5 area)
neighborhood = ['NAmes', 'CollgCr', 'OldTown', 'Edwards', 'Somerst']
neigh_z_score = {}
for i in neighborhood:
    arr = houses.loc[houses['Neighborhood']==i, 'SalePrice']
    neigh_z_score[i] = z_score(200000, arr)

# kde chart for sales Area
houses[''].plot.kde(xlim = (houses['SalePrice'].min(),
                                    houses['SalePrice'].max())
                    )

# making kde chart with z-score of each data point
mean = sum(houses['SalePrice'])/len(houses['SalePrice'])
std_dev = std(houses['SalePrice'])

houses['z_prices'] = houses['SalePrice'].apply(lambda x: (x-mean)/std_dev)

plt.figure(figsize = (11,3.5))
plt.subplot(1,2,1)
houses['z_prices'].plot.kde(xlim = (houses['z_prices'].min(),
                                houses['z_prices'].max()
                                )
                        )
plt.subplot(1,2,2)
houses['SalePrice'].plot.kde(xlim = (houses['SalePrice'].min(),
                                    houses['SalePrice'].max()
                                     )
                            )
plt.tight_layout() # otherwise the plots will overlay partially

# finding mean and z score of z prices
z_mean_price = sum(houses['z_prices'])/len(houses['z_prices'])
z_stdev_price = houses['z_prices'].std(ddof=0)

# z lot area
mean_lot_area = sum(houses['Lot Area'])/len(houses['Lot Area'])
std_lot_area = houses['Lot Area'].std(ddof=0)
houses['z_lot_area'] = houses['Lot Area'].apply(lambda x: (x-mean_lot_area)/std_lot_area)
z_mean_area = sum(houses['z_lot_area'])/len(houses['z_lot_area'])
z_stdev_area = houses['z_lot_area'].std(ddof=0)

'''
In the last exercise, the mean values were both extremely close to 0. For instance, 
we got a mean of -1.1429992333726227e-16 (notice the e-16 at the end) for the z-scores 
distribution of the SalePrice column. This number uses scientific notation to abbreviate 
what in full would be -0.0000000000000001429992333726227. Also, both the standard 
deviations were also very close to 1: 1.0000000000000002 and 0.9999999999999997.

In fact, for every distribution of z-scores, the mean is always 0 and the standard 
deviation is always 1. We got slightly different values in the previous exercise because 
of small rounding errors.
A distribution of z-scores is often called a standard distribution (remember that 
z-scores are also called standard scores).
'''


# standardizing the array population
population = [0,8,0,8]
mean_pop = sum(population)/len(population)
std_pop = std(population, ddof=0)
z_population = []
for i in population:
    z_population.append((i-mean_pop)/std_pop)
             
mean_z = sum(z_population)/len(z_population)
std_z = std(z_population, ddof=0)

# treating population as the sample of population and using bassel correction
# and finding the mean and std deviation of standard distributions
sample = [0,8,0,8]
mean_sample = sum(sample)/len(sample)
std_sample = std(sample, ddof=1)
z_sample = []
for i in sample:
    z_sample.append((i-mean_sample)/std_sample)
             
mean_sample = sum(z_sample)/len(z_sample)
std_sample = std(z_sample, ddof=1)
