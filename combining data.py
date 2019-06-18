# import module
import pandas as pd
import numpy as np

# read file
happiness_2015 = pd.read_csv('D:/Study/Dataquest/Data Sets/World_Happiness_2015.csv')
happiness_2017 = pd.read_csv('D:/Study/Dataquest/Data Sets/World_Happiness_2017.csv')
# adding year column in the data to identify the data
happiness_2015['year']=2015
happiness_2017['year']=2017
# taking subset of datasets
head_2015 = happiness_2015[['Country', 'year', 'Happiness Score']].head(3)
head_2017 = happiness_2017[['Country', 'year', 'Happiness.Score']].head(3)
# concating the data along rows and columns
concat_axis0 = pd.concat([head_2015, head_2017], axis=0)
concat_axis1 = pd.concat([head_2015, head_2017], axis=1)
question1 = concat_axis0.shape[0]
question2 = concat_axis1.shape[0]
''' If you look into the combined data frame closely,
the index of concat_axis0 and concat_axis1 is duplicating
This could be dangorous in case we are calling/performing some action based on index
'''
concat_axis0_index = pd.concat([head_2015, head_2017], ignore_index=True)

''' There is anothe alternative to concat,
That is merge function. It is good to join the very large dataset.
Merge can join only two dataset at a time. And it works only for axis = 1
Merge acts as a SQL join
'''
merged = pd.merge(left=three_2015, right=three_2016, on='Country')
''' Left, right and inner joined can be achived using how arguments
concat function always performs outer join
'''
merged_left = pd.merge(left=three_2015, right=three_2016, how='left', on='Country')
merged_updated = pd.merge(left=three_2016, right=three_2015, how = 'left', on='Country')
merged_suffixes = pd.merge(left=three_2015, right=three_2016, how='left', on='Country', suffixes=('_2015', '_2016'))
merged_updated_suffixes = pd.merge(left=three_2016, right=three_2015, how='left', on='Country', suffixes=('_2016', '_2015'))

''' merge on index value'''
merge_index = pd.merge(left = four_2015,right = three_2016, left_index = True, right_index = True, suffixes = ('_2015','_2016'))
merge_index_left = pd.merge(left=four_2015, right=three_2016, how='left', left_index=True
                       ,right_index=True, suffixes=('_2015', '_2016'))

''' for more details
https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
'''