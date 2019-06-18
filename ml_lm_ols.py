# import module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import file
data = pd.read_table("D:/Study/Dataquest/Data sets/AmesHousing.txt", sep='\t')
train = data[0:1460]
test = data[1460:]

features = ['Wood Deck SF', 'Fireplaces', 'Full Bath', '1st Flr SF', 'Garage Area',
       'Gr Liv Area', 'Overall Qual']

X = train[features]
y = train['SalePrice']
first_term = np.linalg.inv(
        np.dot(
            np.transpose(X), 
            X
        )
    )
second_term = np.dot(
        np.transpose(X),
        y
    )

ols_estimation = np.dot(first_term, second_term)
print(ols_estimation)