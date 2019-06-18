# import module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rand
from numpy import mean
weight = pd.read_table('D:/Study/Dataquest/Data Sets/weight_loss.csv', sep=',')
'''
we have two state in hypothesis testing our null and alternative hypotheses.
Our null hypothesis should describe the default position of skepticism, which is that 
there's no statistically significant difference of given action/input.
Put another way, it should state that any difference is due to random chance. 
Our alternative hypothesis should state that there is in fact a statistically significant 
difference between the outcomes.
'''

mean_group_a = np.mean(weight['3'])
mean_group_b = np.mean(weight['5'])

plt.plot(weight['3'])
plt.show()
plt.plot(weight['5'])
plt.show()

plt.hist(weight['3'])
plt.show()
plt.hist(weight['5'])
plt.show()
'''
Now that we have a test statistic, we need to decide on a statistical test. 
The purpose of a statistical test is to work out the likelihood that the result 
we achieved was due to random chance.
The permutation test is a statistical test that involves simulating rerunning the study 
many times and recalculating the test statistic for each iteration. The goal is to 
calculate a distribution of the test statistics over these many iterations. 
This distribution is called the sampling distribution and it approximates the full range 
of possible test statistics under the null hypothesis. We can then benchmark the test 
statistic we observed in the data (a mean difference of 2.52) to determine how likely 
it is to observe this mean difference under the null hypothesis. If the null hypothesis 
is true, that the weight loss pill doesn't help people lose more weight, than the observed 
mean difference of 2.52 should be quite common in the sampling distribution. If it's 
instead extremely rare, then we accept the alternative hypothesis instead.
'''
all_values = weight['3'].tolist()+weight['5'].tolist()
mean_differences = []
for i in range(1000):
    group_a = []
    group_b = []
    for val in all_values:
        rand_val = rand.rand()
        if(rand_val < 0.5):
            group_a.append(val)
        else:
            group_b.append(val)
            
    iteration_mean_differences = mean(group_b)-mean(group_a)
    mean_differences.append(iteration_mean_differences)
    

plt.hist(mean_differences)
plt.show()

# some random dictionary code
empty = {}

# Since "a" isn't a key in empty, the value False is returned.
key_a = empty.get("a", False)

empty["b"] = "boat"

# key_b is the value for the key "b" in empty.
key_b = empty.get("b", False)
# "boat" is assigned to key_b.


# some other code
empty = {"c": 1}
if empty.get("c", False):
    # If in the dictionary, grab the value, increment by 1, reassign.
    val = empty.get("c")
    inc = val + 1
    empty["c"] = inc
else:
    # If not in the dictionary, assign `1` as the value to that key.
    empty["c"] = 1
    
    

# let's begin
sampling_distribution = {}
for i in mean_differences:
    if sampling_distribution.get(i, False):
       val = sampling_distribution.get(i)
       sampling_distribution[i] = val+1
    else:
        sampling_distribution[i] = 1
        

# we could have done above thing with below piece of code
sampling_distribution2 = {}
for i in mean_differences:
    if i in sampling_distribution2:
        sampling_distribution2[i] += 1
    else:
        sampling_distribution2[i] = 1
        
# checking if both piece of code return same output
print(sampling_distribution==sampling_distribution2)

'''
We can now use the sampling distribution to determine the number of times a value of 2.52
or higher appeared in our simulations. If we then divide that frequency by 1000, 
we'll have the probability of observing a mean difference of 2.52 or higher purely 
due to random chance.

This probability is called the p value. 

If this value is high, it means that the difference in the amount of weight both 
groups lost could have easily happened randomly and the weight loss pills probably 
didn't play a role. On the other hand, a low p value implies that there's an incredibly 
small probability that the mean difference we observed was because of random chance.

The most common p value threshold is 0.05 or 5%
'''

frequencies = []
for i in sampling_distribution:
    if i > 2.52:
        frequencies.append(sampling_distribution[i])

p_value = sum(frequencies)/1000

'''
The p value threshold you set can also affect the conclusion you reach.
If you set too high of a p value threshold, you may accept the alternative hypothesis 
incorrectly and reject the null hypothesis. This is known as a type I error.
If you set too low of a p value threshold, you may reject the alternative hypothesis 
incorrectly in favor of accepting the null hypothesis. This is known as a type II error.
'''