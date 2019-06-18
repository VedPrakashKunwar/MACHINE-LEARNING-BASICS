############################ import data #################################
import pandas as pd
df = pd.read_table("D:/Study/Dataquest/Data sets/chopsticks.csv", sep=',')
chopsticks = df.copy().values.tolist()

# create trial classs
class Trial(object):
    def __init__(self, data):
        self.efficiency = float(data[0])
        self.individual = int(data[1])
        self.chopstick_length = int(data[2])
        
# initiate the trial class
first_trial = Trial(chopsticks[0])

# create the chopstic class
class Chopstick(object):
    def __init__(self, length):
        self.length = length
        self.trials = []
        for row in chopsticks:
            if int(row[2]) == self.length:
                self.trials.append(Trial(row))
        
medium_chopstick = Chopstick(240)
mini_chopstick = Chopstick(100)
