# import module
from numpy.random import randint, seed
import pandas as pd
import matplotlib.pyplot as plt
houses = pd.read_csv('D:/Study/Dataquest/Data Sets/AmesHousing_1.txt', sep='\t')

# get year data
grouped = houses.groupby('Yr Sold')
agg_data = grouped.agg({ 'Order':'nunique', 'SalePrice':'mean'})

# weighted mean
def weighted_mean(list1, list2):
    if len(list1) == len(list2):
        wt = 0
        sp = 0
        for i in range(len(list1)):
            




# weighted mean 
def weighted_mean(distribution, weights):
    weighted_sum = []
    for mean, weight in zip(distribution, weights):
        weighted_sum.append(mean * weight)
    
    return sum(weighted_sum) / sum(weights)

weighted_mean_function = weighted_mean(houses_per_year['Mean Price'],
                                       houses_per_year['Houses Sold'])

from numpy import average
weighted_mean_numpy = average(houses_per_year['Mean Price'],
        weights = houses_per_year['Houses Sold'])

equal = round(weighted_mean_function, 10) == round(weighted_mean_numpy, 10)



# median of totRms AbvGrd
rooms = houses['TotRms AbvGrd'].copy()
rooms_sorted = rooms.replace({'10 or more': 10}).astype(int).sort_values()
middle_indices = [len(rooms)/2-1, len(rooms)/2]
median_rooms = rooms_sorted[middle_indices].sum()/2
median_roomss = rooms_sorted.iloc[middle_indices].sum()/2

# median vs mean -- part 1
import matplotlib.pyplot as plt
houses['Lot Area'].plot.box()
plt.show()
houses['SalePrice'].plot.box()
plt.show()
lotarea_difference = houses['Lot Area'].mean() - houses['Lot Area'].median()
saleprice_difference = houses['SalePrice'].mean() - houses['SalePrice'].median()

# median vs mena -- part 2
mean = houses['Overall Cond'].mean()
median = houses['Overall Cond'].median()
houses['Overall Cond'].plot.hist()

# overall condition -- ordinal variable
over_cond = houses['Overall Cond'].unique()

