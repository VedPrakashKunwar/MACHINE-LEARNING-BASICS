# import module
import pandas as pd
import numpy as np

############################ import data #################################
data = pd.read_table("D:/Study/Dataquest/Data sets/AmesHousing.txt", sep='\t')

# selecting column with less than 25% null value
col_null = data.isnull().sum()/2930
col_null = col_null[col_null <= 0.25]

# looking into the numerical columns
num_col = data.select_dtypes(include=['int32', 'int64', 'float64', 'float32']).columns
corrs = data.corr().loc[:, 'SalePrice'].abs()