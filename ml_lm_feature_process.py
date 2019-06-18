# import module
import pandas as pd
import numpy as np

# read data
data = pd.read_table("D:/Study/Dataquest/Data sets/AmesHousing.txt", sep='\t')

# dividing data into train and test set
train = data[0:1460]
test = data[1460:]

# looking at the value with zero null value
col = train.isnull().sum()[train.isnull().sum() == 0].index
df_no_mv = train[col]

# convert every text column into numerical column
text_cols = df_no_mv.select_dtypes(include=['object']).columns

for col in text_cols:
    print(col+":", len(train[col].unique()))
    train[col] = train[col].astype('category')
    
# check data of one of the categorical column just converted
train['Utilities'].value_counts()
train['Utilities'].cat.codes.value_counts()

# convert all the text column into the dummy varaible
text_cols = df_no_mv.select_dtypes(include=['object']).columns
for col in text_cols:
    dummy_cols = pd.get_dummies(train[col])
    train = pd.concat([train, dummy_cols], axis=1)
    del train[col]
    
# Year Remove/add does mean much for the house price
# instead using the difference between remodelling and year sold
train['years_until_remod'] = train['Year Remod/Add'] - train['Year Built']

train_null_counts = train.isnull().sum()
df_missing_values = train[train_null_counts[(train_null_counts>0) & (train_null_counts<584)].index]

print(df_missing_values.isnull().sum())
print(df_missing_values.dtypes)
float_cols = df_missing_values.select_dtypes(include=['float'])
float_cols = float_cols.fillna(float_cols.mean())
print(float_cols.isnull().sum())