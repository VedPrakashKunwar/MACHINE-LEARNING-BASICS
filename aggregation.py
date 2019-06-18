''' official docs of group by
***https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html****
refer this in case of any doubts

also a good read will be the below source on pivot
***https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot_table.html***
'''

# group by aggregation
import pandas as pd

# read file
df = pd.read_csv('D:/Study/Dataquest/Data Sets/World_Happiness_2015.csv')

# grouping data without group by 
Region = df['Region'].unique()
mean_happiness = {}
for reg in Region:
    mean_happiness[reg] = df.loc[df['Region']==reg, 'Happiness Score'].mean()
print(mean_happiness)
'''
There is three steps in group by:
    1. split the data
    2. apply the aggregation method i.e-mean, max
    3. combine the data
'''
# looking into pandas group by
grouped = df.groupby('Region')
auz_nz = grouped.get_group('Australia and New Zealand')
groups = grouped.groups
na = groups['North America']
print(df.loc[na, :])
print(grouped.size())
# group by methods
means = grouped.mean()
sums = grouped.sum()
sizes = grouped.size()
counts = grouped.count()
min = grouped.min()
max = grouped.max()
# mean happiness score
happy_grouped = grouped['Happiness Score']
happy_mean = happy_grouped.mean()
# calculating more than one aggreagation on same column
import numpy as np
grouped = df.groupby('Region')
happy_grouped = grouped['Happiness Score']
def dif(group):
    return (group.max() - group.mean())
happy_mean_max = happy_grouped.agg([np.mean, np.max])
# we can also pass the user defined function in agg
mean_max_dif = happy_grouped.agg(dif) 
'''
Pivot function is same as the pivot function in excel
Here we get output as data frame
We also gets an additional column All, by setting margin = True
similary as in Excel
'''
# pivot function
pv_happiness = df.pivot_table(values='Happiness Score', index='Region', aggfunc=np.mean, margins=True)
pv_happiness.plot(kind='barh', xlim=(0,10), title='Mean Happiness Scores by Region', legend= False)
world_mean_happiness = df['Happiness Score'].mean()
# happiness2015.pivot_table(['Happiness Score', 'Family'], 'Region')
# happiness2015.pivot_table('Happiness Score', 'Region', aggfunc=[np.mean, np.min , np.max], margins=True)
# muliple aggregation
happy_family_stats = df.groupby('Region')[['Family', 'Happiness Score']].agg([np.min, np.max, np.mean])
pv_happy_family_stats = df.pivot_table(['Family', 'Happiness Score'], 'Region', aggfunc=[np.min,np.max,np.mean], margins=True)