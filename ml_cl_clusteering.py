# import module
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
############################ import data #################################
votes = pd.read_table("D:/Study/Dataquest/Data sets/114_congress.csv", sep=',')

# exploring the data
print(votes.info())
# senartor by party
print(votes['party'].value_counts())
print(votes.loc[:,'00001':'00047'].mean())
print(euclidean_distances(votes.iloc[0,3:].values.reshape(1, -1), votes.iloc[1, 3:].values.reshape(1, -1)))

# applying  k-means
kmeans_model = KMeans(n_clusters=2, random_state=1)
senator_distances = kmeans_model.fit_transform(votes.iloc[:, 3:])
labels = kmeans_model.labels_
print(pd.crosstab(labels, votes["party"]))
# looking into the three democrates party member
votes[(labels == 1) & (votes["party"] == "D")]

# ploting  distances
plt.scatter(senator_distances[:,0], senator_distances[:,1], c=labels, linewidths=0)
plt.show()

'''We cube the distances so that we can get a good amount of separation between the extremists who are farther away from a party, who have distances that look like extremist = [3.4, .24], and moderates, whose distances look like moderate = [2.6, 2]. If we left the distances as is, we'd end up with 3.4 + .24 = 3.64, and 2.6 + 2 = 4.6, which would make the moderate, who is between both parties, seem extreme. If we cube, we instead end up with 3.4 ** 3 + .24 ** 3 = 39.3, and 2.6 ** 3 + 2 ** 3 = 25.5, which correctly identifies the extremist.
'''

senator_distances = senator_distances**3
extremism = np.sum(senator_distances, axis = 1)
votes['extremism'] = extremism
# sort votes by extremist
votes.sort_values(by=['extremism'], ascending=False, inplace=True)
print(votes['name'].head(10))