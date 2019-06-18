# import module
import pandas as pd

# import dataset
happiness_2015 = pd.read_csv('D:/Study/Dataquest/Data Sets/World_Happiness_2015.csv')
col = happiness_2015.columns
mapping = {'Economy (GDP per Capita)': 'Economy'
           , 'Health (Life Expectancy)': 'Health'
           , 'Trust (Government Corruption)': 'Trust'
           }
''' 
In this excercising we are seeing the most immportannt factor
deciding the factor of happinness
The method used here are:
    1. Series.map()
    2. Series.apply()
    3. DataFrame.applymap()
    4. DataFrame.apply()
    5. pd.melt()
'''

# rename the column with mapping
happiness_2015 = happiness_2015.rename(mapping, axis=1)

'''
When we reviewed happiness2015 in the last screen, 
you may have noticed that each of the "factor" columns consists of numbers.

'''

# make user-defined function
def val(v):
    if v < 1:
        return 'Low'
    else:
        return 'High'

hap_econ_map = happiness_2015['Economy'].map(val)
hap_econ_apply = happiness_2015['Economy'].apply(val)
equal = hap_econ_map.equals(hap_econ_apply)
happiness_2015['Economy Impact'] = happiness_2015['Economy'].map(val)

# make user-defined function
def val1(v, x):
    if v < x:
        return 'Low'
    else:
        return 'High'
    
hap_econ_apply1 = happiness_2015['Economy'].apply(val1, x=0.8)