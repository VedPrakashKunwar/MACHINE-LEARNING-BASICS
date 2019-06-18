# import module
from numpy.random import randint, seed
import pandas as pd
import matplotlib.pyplot as plt
houses = pd.read_csv('D:/Study/Dataquest/Data Sets/AmesHousing_1.txt', sep='\t')

sample_size = 5
parameter = houses['SalePrice'].mean()
sampling_error = []
sampling_sizes = []
for i in range(101):
    s = sample_size + 29*i
    sampling_sizes.append(s)
    sample = houses['SalePrice'].sample(s, random_state = i)
    sampling_error.append(parameter-sample.mean())
    
# plot sampling error v/s sampling size
plt.scatter(sampling_sizes, sampling_error)
plt.axhline(0)
plt.axvline(2930)
plt.xlabel('Sample size')
plt.ylabel('Sampling error')

''' 
            plotting histogram
''''
mean = []
for i in range(10000):
    sample = houses['SalePrice'].sample(100, random_state = i)
    mean.append(sample.mean())
    
plt.hist(mean)
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.xlim(0, 500000)
plt.axvline(houses['SalePrice'].mean())

# mean
distribution = [0,2,3,3,3,4,13]
mean = sum(distribution)/len(distribution)
above = 0
below = 0
for val in distribution:
    if val <= mean:
        below += (mean-val)
    else:
        above += (val-mean)

print(above==below)

# random list
equal_distances = 0
for i in range(0, 5000):
    seed(i)
    lst = randint(0, 1000, size=10)
    mean = sum(lst)/len(lst)
    above = 0
    below = 0
    for val in lst:
        if val <= mean:
            below += (mean-val)
        else:
            above += (val-mean)
    if round(above,1) == round(below, 1):
        equal_distances += 1
    else:
        print(i)
        print(above)
        print(below)
