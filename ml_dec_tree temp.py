# import module
import numpy as np
import math
import pandas as pd

############################ import data #################################
income = pd.read_table("D:/Study/Dataquest/Data sets/income1.csv", sep=',')

# looking into the data
print(income.info())
print(income.isnull().sum())
cols = income.columns
text_cols = income.select_dtypes(include='object').columns

for col in text_cols:
    print('_____**',col,'**_____')
    print(income[col].unique())
    print()