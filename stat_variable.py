''' This is the python code 
from variable in the statstics. 
The variable in statistics means one which varies.
Variable in the programming pragdim is different from one of the statstics.
A variable can describe quantities and qualities.
qualitative variables or categorical variables can be numerical too.
Similarly, quantitative variable can be of text type.
For two quantitative varible value we can say:
    1.We can tell the size of the difference.
    2.We can which is greater and by how much.
    
Nominal and Ordinal Scale are two scale.
In both case we case we can deduce if the value is different but we can't deduce the amount of difference.
In case of Ordinal scale we can deduce which category is bigger like hieght- small, medium and large.
but in team like RCB, SRH we can't deduce which is larger/smaller. 

Interval and Ratio scale are two scale.
In Ratio scale if value is zero it indicates the lack of any value. i.e- wieght = 0 means no weight
In Interval scale 0 does't mean absence. Like weight_deviation = 0 then it means wieght is the mean of weight of population/sample.

quantitative variables can be measured on ordinal, interval, or ratio scales. In this screen, we zoom in on variables measured on interval and ratio scales.
'''

# import module
import pandas as pd
import matplotlib.pyplot as plt

# import dataset
wnba = pd.read_csv('D:/Study/Dataquest/Data Sets/wnba.csv')
variables = {'Name': 'qualitative', 'Team': 'qualitative', 'Pos': 'qualitative', 'Height': 'quantitative', 'BMI': 'quantitative',
             'Birth_Place': 'quantitative', 'Birthdate': 'qualitative', 'Age': 'quantitative', 'College': 'qualitative', 'Experience': 'quantitative',
             'Games Played': 'quantitative', 'MIN': 'quantitative', 'FGM': 'quantitative', 'FGA': 'quantitative',
             '3PA': 'quantitative', 'FTM': 'quantitative', 'FTA': 'quantitative', 'FT%': 'quantitative', 'OREB': 'quantitative', 'DREB': 'quantitative',
             'REB': 'quantitative', 'AST': 'quantitative', 'PTS': 'quantitative'}
# get all the qualitative variables
#columns = list(variables.keys())
#value = list(variables.values())
#qual_var = columns[value=='']

# columns in wnba
col = wnba.columns