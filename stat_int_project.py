# import module
import pandas as pd
import numpy as np

# read datasets
df = pd.read_csv('D:/Study/Dataquest/Data sets/2017-fCC-New-Coders-Survey-Data.csv')

# look into data
col = df.columns
print(df.shape)
print(df.head(5))
print(df.isnull().sum()*100/18175)

# job intersted in
print(df['JobRoleInterest'].unique())
df['JobRoleInterest'] = df['JobRoleInterest'].str.lstrip().str.rstrip()
print(df['JobRoleInterest'].value_counts())