''' This is the python code 
from sampling of data
'''

# import module
import pandas as pd
import matplotlib.pyplot as plt

# import dataset
wnba = pd.read_csv('D:/Study/Dataquest/Data Sets/wnba.csv')

# sampling
wnba_sample = wnba.sample(30)

# demonstarating and discrepancy in the sampling
population_mean = wnba['PTS'].mean()
mean_pts = []
for i in range(0,100):
    mean_pts.append(wnba['PTS'].sample(10, random_state=i).mean())

# plot the chart
plt.scatter(range(1, 101), mean_pts)
plt.axhline(population_mean)

# points_per_game
wnba['points_per_game'] = wnba['PTS']/wnba['Games Played']
# stratified sampling
strata = wnba['Pos'].unique()
points_per_position = {}
for i in strata:
    globals()['strata_%s' % i] = wnba[wnba['Pos']==i].sample(10, random_state=0)
    points_per_position[i] = wnba.loc[wnba['Pos']==i, 'points_per_game'].sample(10, random_state=0).mean()
    
# returning the key with max value
def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

max_value = keywithmaxval(points_per_position)
full_starta = pd.DataFrame()
# statifing based on the match played
for i in range(100):
    starta_0_12 = wnba.loc[(wnba['Games Played'] > 0) & (wnba['Games Played'] < 13)].sample(1, random_state=i)
    starta_13_22 = wnba.loc[(wnba['Games Played'] > 12) & (wnba['Games Played'] < 23)].sample(2, random_state=i)
    starta_23 = wnba.loc[wnba['Games Played'] > 22].sample(7, random_state=i)
    full_starta = pd.concat([full_starta, starta_0_12, starta_13_22, starta_23], axis=0)
    
# cluster sampling
clusters = pd.Series(wnba['Team'].unique()).sample(4, random_state=0)
sample = pd.DataFrame()

for team in clusters:
    sample = sample.append(wnba[wnba['Team'] == team])

# sampling error
sampling_error_height = wnba['Height'].mean()-sample['Height'].mean()
sampling_error_age = wnba['Age'].mean() - sample['Age'].mean()
sampling_error_BMI = wnba['BMI'].mean() - sample['BMI'].mean()
sampling_error_points = wnba['PTS'].mean() - sample['PTS'].mean()