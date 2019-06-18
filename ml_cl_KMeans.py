# import module
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.cluster import KMeans
############################ import data #################################
nba = pd.read_table("D:/Study/Dataquest/Data sets/nba_2013.csv", sep=',')

'''
some of the columns
player -- name of the player
pos -- the position of the player
g -- number of games the player was in
pts -- total points the player scored
fg. -- field goal percentage
ft. -- free throw percentage
'''

# looking into data
print(nba.info())
print(nba.isnull().sum()[nba.isnull().sum() > 0])
description = nba.describe(include='all')

# looking for point gaurd in data
point_guards = nba.loc[nba['pos']=='PG'].copy()
# creating point per games
# points per game = total points(pts)/number of games(g)
point_guards['ppg'] = point_guards['pts']/point_guards['g']
# Sanity check, make sure ppg = pts/g
point_guards[['pts', 'g', 'ppg']].head(5)
# creating assist turnover ratio 
# atr = assist(ast)/turnover(tov)
# droping player with 0 turnover
point_guards = point_guards[point_guards['tov'] != 0]
point_guards['atr'] = point_guards['ast']/point_guards['tov']
# Sanity check, make sure atr = ast/tov
point_guards[['atr', 'ast', 'tov']].head(5)
# creating plot for ppg and atr
plt.scatter(point_guards['ppg'], point_guards['atr'], c='r', alpha=0.3)
plt.title('Points Per Game v/s Assit Turnover Ratio')
plt.xlabel('Point Per Game')
plt.ylabel('Assists Turnover Ratio')
plt.show()

# creating K-means model for K = 5
num_clusters = 5
# Use numpy's random function to generate a list, length: num_clusters, of indices
random_initial_points = np.random.choice(point_guards.index, size=num_clusters)
# Use the random indices to create the centroids
centroids = point_guards.loc[random_initial_points]

plt.scatter(point_guards['ppg'], point_guards['atr'], c='yellow')
plt.scatter(centroids['ppg'], centroids['atr'], c='red')
plt.title("Centroids")
plt.xlabel('Points Per Game', fontsize=13)
plt.ylabel('Assist Turnover Ratio', fontsize=13)
plt.show()

# storing centroid coordinates with respective centroid id in dictionary
def centroids_to_dict(centroids):
    dictionary = dict()
    # iterating counter we use for generating cluster id
    counter = 0
    
    # iterating over the clusters
    for index, rows in centroids.iterrows():
        coordinates = [rows['ppg'], rows['atr']]
        dictionary[counter] = coordinates
        counter += 1
    return dictionary

centroid_dict = centroids_to_dict(centroids)

''' Before we can assign players to clusters, we need a way to compare the ppg and atr values of the players with each cluster's centroids. Euclidean distance is the most common technique used in data science for measuring distance between vectors and works extremely well in 2 and 3 dimensions. While in higher dimensions, Euclidean distance can be misleading, in 2 dimensions Euclidean distance is essentially the Pythagorean theorem.
'''
def calculate_distance(centroid, player_value):
    root_distance = 0
    
    for x in range(0, len(centroid)):
        diff = centroid[x] - player_value[x]
        #print(centroid[x]) 
        #print(player_value[x])
        squared_difference = diff**2
        root_distance += squared_difference
    
    euclid_distance = math.sqrt(root_distance)
    return euclid_distance

# testing calculate_distance function
q = [6, 2]
p = [3, 6]
print(calculate_distance(q, p))

def assign_to_cluster(row):
    lowest_centroid = -1
    lowest_distance = -1
    
    for cluster_id, centroid in centroid_dict.items():
        df_row = [row['ppg'], row['atr']]
        euclidean_distance = calculate_distance(centroid, df_row)
        if lowest_distance == -1:
            lowest_distance = euclidean_distance
            lowest_centroid = cluster_id
        elif lowest_distance > euclidean_distance:
            lowest_distance = euclidean_distance
            lowest_centroid = cluster_id
    return lowest_centroid

point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)

# Visualizing clusters
def visualize_clusters(df, num_clusters):
    colors = ['m', 'g', 'r', 'y', 'o', 'y', 'k']

    for n in range(num_clusters):
        clustered_df = df[df['cluster'] == n]
        plt.scatter(clustered_df['ppg'], clustered_df['atr'], c=colors[n-1], alpha=0.5)
        plt.xlabel('Points Per Game', fontsize=13)
        plt.ylabel('Assist Turnover Ratio', fontsize=13)
    plt.show()

visualize_clusters(point_guards, 5)

# recalculate the cluster
def recalculate_centroids(df):
    new_centroids_dict = dict()
    num_clusters = 5
    # 0..1...2...3...4
    for cluster_id in range(0, num_clusters):
        # Finish the logic
        new_centroids_dict[cluster_id] = [df.loc[df['cluster']==cluster_id, 'ppg'].mean(),
                                         df.loc[df['cluster']==cluster_id, 'atr'].mean()]
        return new_centroids_dict

centroids_dict = recalculate_centroids(point_guards)

# reasigning the clusters
point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)
visualize_clusters(point_guards, num_clusters)

# recalculate the clusters
centroids_dict = recalculate_centroids(point_guards)
point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)
visualize_clusters(point_guards, num_clusters)

# clustering using the sklearn

kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(point_guards[['ppg', 'atr']])
point_guards['cluster'] = kmeans.labels_

visualize_clusters(point_guards, num_clusters)