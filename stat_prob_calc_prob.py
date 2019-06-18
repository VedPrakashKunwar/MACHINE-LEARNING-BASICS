# import module
import pandas as pd
import math
import matplotlib.pyplot as plt
from scipy import linspace
from scipy.stats import binom
bikes = pd.read_table('D:/Study/Dataquest/Data Sets/bike_rental_day.csv', sep=',')

# probability that more than 4000 bike rented on any day
probability_over_4000 = bikes[bikes['cnt']>4000].shape[0]/bikes.shape[0]

# Below from here is the code for distribution

# probability of K outcome out of n event of binomial probablity
def prob_k_n(N, k, p):
    q = 1-p
    good = p**k
    bad = q**(N-k)
    total_outcome = math.factorial(N)
    fav_outcome = math.factorial(k)
    non_fav_outcome = math.factorial(N-k)
    probability = good*bad*total_outcome/fav_outcome/non_fav_outcome
    return probability

# loop for 30 days, with N = 30 and k = [0, 30]
p = bikes[bikes['cnt']>5000].shape[0]/bikes.shape[0]
probability = []
for i in range(31):
    probability.append(prob_k_n(30, i, p))
    
# ploting the probability chart
plt.bar(list(range(31)), probability)
plt.show()

# doing above thing with 
outcome_counts = linspace(0,30,31)
# Create the binomial probabilities, one for each entry in outcome_counts.
dist = binom.pmf(outcome_counts,30,0.39)
plt.bar(outcome_counts, dist)
plt.show()

loops = list(range(10))
outcome_counts = binom.pmf(loops, 30, 0.39)
plt.bar(loops, outcome_counts)
plt.show()

# cummulative density function
outcome_counts = linspace(0,30,31)
cdf_val = binom.cdf(outcome_counts, 30, 0.39)
plt.plot(outcome_counts, cdf_val)
plt.show()

'''
mean of probability distribution function = N*p
standard deviation of probability distribution function = (N*p*q)**(0.5)
'''
left_16 = binom.cdf(16, 30, 0.39)
right_16 = 1-left_16