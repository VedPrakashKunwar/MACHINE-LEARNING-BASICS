# import module
import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange

pd.options.display.max_rows = 200
pd.options.display.max_columns = 50

# import dataset
wnba = pd.read_csv('D:/Study/Dataquest/Data Sets/wnba.csv')

# plot frequency plots
wnba['Team'].value_counts().plot.bar(rot=-45, title='Player by Team')
wnba['Pos'].value_counts().plot.pie()
# make plot aesthetic again
wnba['Pos'].value_counts().plot.pie(figsize = (6,6), autopct = '%.1f%%')
plt.ylabel('')
# https://docs.python.org/3/library/string.html#format-specification-mini-language
# histograms
wnba['PTS'].plot.hist()
wnba['PTS'].value_counts(bins = 10).sort_index()
wnba['PTS'].plot.hist(grid = True, xticks = arange(2,585,58.2), rot = 30)
wnba['Games Played'].plot.hist()
wnba['PTS'].plot.hist(range = (1,600), bins = 6)
wnba['Games Played'].plot.hist(range=(1, 32), bins = 8, title='The distribution of players by games played')
plt.xlabel('Games played')
'''
If the tail points to the left, then the distribution is said to be left skewed.
If the tail points to the right, then the distribution is right skewed.
If the shape of the histogram is symmetrical, then we say that we have a symmetrical distribution
'''