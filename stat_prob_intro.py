# import module
import pandas as pd
flags = pd.read_table('D:/Study/Dataquest/Data Sets/flags.csv', sep=',')

# looking into the data
print(flags.shape) 
# country with highest bar
bars = flags.sort_values("bars", ascending=False)
most_bars_country = bars["name"].iloc[0]
# country with highest population
population = flags.sort_values("population", ascending=False)
highest_population_country = population["name"].iloc[0]

# probability of orange and more than one strips
total_countries = flags.shape[0]
orange_probability = flags['orange'].value_counts().sort_index()[1]/total_countries
stripe_probability = flags[flags['stripes']>1].shape[0]/total_countries

# probability of three red in a row
# Remember that whether a flag has red in it or not is in the `red` column.
red_population = flags[flags['red'] == 1].shape[0]
population = flags.shape[0]

# probablity
three_red = (red_population/population)*((red_population-1)/(population-1))*((red_population-2)/(population-2))

# find the probabilty of no between [1, 18000] divisible by 70 and 100
hundred = list(range(100, 18001, 100))
seventy = list(range(70, 18001, 70))
hundred_prob=len(hundred)/18000
seventy_prob=len(seventy)/18000

# probablity of red or orange and strip and bar
red_or_orange=flags[(flags['red']==1)|(flags['orange']==1)].shape[0]/flags.shape[0]
stripes_or_bars=flags[(flags['stripes']>0)|(flags['bars'])>0].shape[0]/flags.shape[0]