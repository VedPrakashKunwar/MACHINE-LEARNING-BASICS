'''

'''

# import module
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_rows = 200
pd.options.display.max_columns = 50

# import dataset
wnba = pd.read_csv('D:/Study/Dataquest/Data Sets/wnba.csv')
# frequency table
freq_distro_pos = wnba['Pos'].value_counts()
freq_distro_height = wnba['Height'].value_counts()
age_ascending = wnba['Age'].value_counts().sort_index(ascending=True)
age_descending = wnba['Age'].value_counts().sort_index(ascending=False)
''' sorting index will work for the interval and ratio variable but for ordinal and nominal 
variable it won't work. so we have to sort them manually
'''
def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if (20 < row['PTS'] <=  80):
        return 'few points'
    if (80 < row['PTS'] <=  150):
        return 'many, but below average'
    if (150 < row['PTS'] <= 300):
        return 'average number of points'
    if (300 < row['PTS'] <=  450):
        return 'more than average'
    else:
        return 'much more than average'
    
wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis = 1)

print(wnba['PTS_ordinal_scale'].value_counts()[['very few points', 'few points', 'many, but below average', 'average number of points']])
print(wnba['PTS_ordinal_scale'].value_counts())
print(wnba['PTS_ordinal_scale'].value_counts().iloc[[3, 1, 2, 0]])

# show propotions
print(wnba['Pos'].value_counts(normalize = True))
print(wnba['Pos'].value_counts(normalize = True) * 100)
proportion_25 = len(wnba[wnba['Age']==25])/len(wnba)
percentage_30 = wnba.loc[wnba['Age']==30, 'Age'].value_counts()/len(wnba)*100
percentage_over_30 = len(wnba[wnba['Age']>=30])/len(wnba)*100
percentage_below_23 = len(wnba[wnba['Age']<=23])/len(wnba)*100

# give percentile 
from scipy.stats import percentileofscore
percentile_rank_half_less = percentileofscore(a=wnba['Games Played'], score=17, kind='weak')
percentage_half_more = 100-percentile_rank_half_less
# to get percentile we can also use the describe function
print(wnba['Age'].describe())
print(wnba['Age'].describe().iloc[3:])
# We may be interested to find the percentiles for percentages other than 25%, 50%, or 75%
print(wnba['Age'].describe(percentiles = [.1, .15, .33, .5, .592, .85, .9]).iloc[3:])
desc_var = wnba['Age'].describe(percentiles=[0.75, 0.5, 0.95]).iloc[4:]
fifty_percentile = desc_var[0]
# dividing continous variable into group
print(wnba['Weight'].value_counts().sort_index())
print(wnba['Weight'].value_counts(bins = 10).sort_index())
'''
Because we group values in a table to get a better sense of frequencies in the distribution, 
the table we generated above is also known as a grouped frequency distribution table. 
Each group (interval) in a grouped frequency distribution table 
is also known as a class interval.
'''
grouped_freq_table = wnba['PTS'].value_counts(bins=10).sort_index(ascending=False)*100/len(wnba)
'''
In some case the we want to make the class interval for the descrete value. When making 
class the class interval may come as real number which doesn't make much sense. So we have
to fix that ourself
'''
intervals = pd.interval_range(start = 0, end = 600, freq = 100)
print(intervals)
gr_freq_table = pd.Series([0,0,0,0,0,0], index = intervals)
print(gr_freq_table)
for value in wnba['PTS']:
    for interval in intervals:
        if value in interval:
            gr_freq_table.loc[interval] += 1
            break
print(gr_freq_table)