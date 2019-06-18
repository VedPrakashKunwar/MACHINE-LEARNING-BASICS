# import module
from numpy.random import randint, seed
import pandas as pd
import matplotlib.pyplot as plt
houses = pd.read_csv('D:/Study/Dataquest/Data Sets/AmesHousing_1.txt', sep='\t')

def mode(array):
    counts = {}
    
    for value in array:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    
    return max(counts, key = counts.get)

mode_function = mode(houses['Land Slope'])
mode_method = houses['Land Slope'].mode()
same = (mode_function == mode_method)

# return both mode and dictionary

def mode_dict(array):
    counts = {}
    for value in array:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    mode = max(counts, key=counts.get)
    print(counts)
    return (mode, counts)

mode= mode_dict(houses['Land Slope'])[0]
value_counts = mode_dict(houses['Land Slope'])[1]

''' 
Mode is used in the case of Nomimal variable and dicrete variable.
There are distributions that can have more than one mode.
For this reason, we call this distribution bimodal (the prefix "bi-" means "twice"). 
If the distribution had only one mode, we'd call it unimodal 
(the prefix "uni-" means "only one").
When a distribution has more than two modes, we say that the distribution is multimodal 
(the prefix "multi-" means many).
We can also have cases when there is no mode at all.
conside the no of bedroom in houses:-   [1, 1, 2, 2, 3, 3, 4, 4]
Each unique value occurs twice in the distribution above, so there's no value 
(or values) that occurs more often than others. For this reason, this distribution 
doesn't have a mode. Contextually, we could say that there's no typical house 
on the market with respect to the number of bedrooms.
The workaround is to organize the continuous variable in a grouped frequency table, 
and select for the mode the midpoint of the class interval (the bin) with the highest 
frequency. This method has its limitations, but it generally gives reasonable answers
'''

# frequency table
intervals = pd.interval_range(start = 0, end = 800000, freq = 100000)
gr_freq_table = pd.Series([0,0,0,0,0,0,0,0], index = intervals)

for value in houses['SalePrice']:
    for interval in intervals:
        if value in interval:
            gr_freq_table.loc[interval] += 1
            break

print(gr_freq_table)
mode = 150000
mean = houses['SalePrice'].mean()
median = houses['SalePrice'].median()

'''
When we plot a histogram or a kernel density plot to visualize the shape of a distribution,
the mode will always be the peak of the distribution
'''

houses['SalePrice'].plot.kde(xlim=(houses['SalePrice'].min(), houses['SalePrice'].max()))
plt.axvline(150000) # mode from above

'''
This distribution is clearly right skewed. Generally, the location of the mode, median and mean is predictable for a right-skewed distribution:

Most values are concentrated in the left body of the distribution where they will form a peak — 
this is where the mode will be.
Remember that the median divides a distribution in two halves of equal length. 
For this reason, the median is usually positioned slightly right from the peak (the mode)
for a right-skewed distribution.
The mean takes into account each value in the distribution, and it will be affected 
by the outliers in the right tail. This will generally pull the mean to the right 
of the median.For a left-skewed distribution, the direction is simply reversed: 
the mean is positioned to the left of the median, and the median to the left of the mode.
https://www.tandfonline.com/doi/full/10.1080/10691898.2005.11910556
'''
houses['SalePrice'].plot.kde(xlim = (houses['SalePrice'].min(),
                                     houses['SalePrice'].max()
                                    )
                            )
plt.axvline(150000, color = 'Green', label = 'Mode')
plt.axvline(houses['SalePrice'].median(), color = 'Black', label = 'Median')
plt.axvline(houses['SalePrice'].mean(), color = 'Orange', label = 'Mean')
plt.legend()


# mo sold
houses['Mo Sold'].plot.kde(xlim = (1, 12))
plt.axvline(houses['Mo Sold'].mode()[0], color = 'green', label = 'Mode')
plt.axvline(houses['Mo Sold'].mean(), color = 'black', label = 'Mean')
plt.axvline(houses['Mo Sold'].median(), color = 'orange', label = 'Median')
plt.legend()