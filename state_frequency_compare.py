# import module
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#from numpy import arange

pd.options.display.max_rows = 200
pd.options.display.max_columns = 50

# import dataset
wnba = pd.read_csv('D:/Study/Dataquest/Data Sets/wnba.csv')

# plot the chart
sns.countplot(x='Team', hue='Pos', data=wnba
             ,order = ['IND', 'ATL', 'NY', 'WAS', 'CHI', 'PHO', 'SEA', 'MIN', 'SAN', 'CON', 'DAL', 'LA']
             , hue_order = ['C', 'F', 'F/C', 'G', 'G/F'])
# the older player will play less game as compared to younger player
wnba['age_mean_relative'] = wnba['Age'].apply(lambda x: 'old' if x >= 27 else 'young')
wnba['min_mean_relative'] = wnba['MIN'].apply(lambda x: 'average or above' if x >= 497 else
                                           'below average')
# testing abouve hypothesis
sns.countplot(x='age_mean_relative', hue='min_mean_relative', data = wnba)
# our hypothesis was wrong as older player will play more game as given in data
# one way to compare two different categroy is to plot them together 
wnba[wnba.Age >= 27]['MIN'].plot.hist(label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.hist(label = 'Young', legend = True)
# as hist overlap we can't seen the value at the back
wnba[wnba.Age >= 27]['MIN'].plot.hist(histtype = 'step', label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.hist(histtype = 'step', label = 'Young', legend = True)
plt.axvline(497, label = 'Average')
plt.legend()
# the plot from above code looks crowded and hard to read/interpret.
# so smoothing of chart will be done
# the smooth chart is called kernel density estimate plot or, shorter, kernel density plot
wnba[wnba.Age >= 27]['MIN'].plot.kde(label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.kde(label = 'Young', legend = True)
plt.axvline(497, label = 'Average')
plt.legend()
# analysing the heigh and position
wnba[wnba.Pos == 'F']['Height'].plot.kde(label = 'F', legend = True)
wnba[wnba.Pos == 'C']['Height'].plot.kde(label = 'C', legend = True)
wnba[wnba.Pos == 'G']['Height'].plot.kde(label = 'G', legend = True)
wnba[wnba.Pos == 'G/F']['Height'].plot.kde(label = 'G/F', legend = True)
wnba[wnba.Pos == 'F/C']['Height'].plot.kde(label = 'F/C', legend = True)
# the above chart is a bit crowded
sns.stripplot(x = 'Pos', y = 'Height', data = wnba)
sns.stripplot(x = 'Pos', y = 'Height', data = wnba, jitter = True)
sns.boxplot(x = 'Pos', y = 'Height', data = wnba)
'''
A value is an outlier if:

It's larger than the upper quartile by 1.5 times the difference between the upper quartile
and the lower quartile (the difference is also called the interquartile range).
It's lower than the lower quartile by 1.5 times the difference between the upper quartile 
and the lower quartile (the difference is also called the interquartile range).
'''
sns.boxplot(wnba[wnba['Pos'] == 'C']['Height'], whis = 4,
           orient = 'vertical', width = .15)

