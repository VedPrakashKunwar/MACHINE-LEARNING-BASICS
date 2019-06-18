 # import module
import pandas as pd
import numpy as np
from scipy.spatial import distance
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
np.random.seed(1)

dc_listings = pd.read_csv("D:/Study/Dataquest/Data sets/dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
train_df = dc_listings.iloc[0:2792]
test_df = dc_listings.iloc[2792:]

def predict_price(new_listing):
    ## DataFrame.copy() performs a deep copy
    temp_df = train_df.copy()
    temp_df['distance'] = temp_df['accommodates'].apply(lambda x: np.abs(x - new_listing))
    temp_df = temp_df.sort_values('distance')
    nearest_neighbor_prices = temp_df.iloc[0:5]['price']
    predicted_price = nearest_neighbor_prices.mean()
    return(predicted_price)


test_df['predicted_price'] = test_df['accommodates'].apply(predict_price)

# data 
print(dc_listings.info())
# removing non-numeric and non-relevant data for now
dc_listings.drop(['room_type', 'city', 'state', 'latitude', 'longitude', 'zipcode'
                  , 'host_acceptance_rate', 'host_listings_count', 'host_response_rate']
    , axis=1, inplace=True)

# checking the null data 
dc_listings.isnull().sum()[dc_listings.isnull().sum()>0]/len(dc_listings)
# as bedroom, bathrooms and beds has very less missing data so we will remove 
# the row with missing value
# as cleaning fee and security deposite is having large missing data so we will 
# remove the columns
dc_listings.drop(['cleaning_fee', 'security_deposit'], axis=1, inplace=True)
dc_listings.dropna(axis=0, inplace=True)
dc_listings.info()
# viewing the spread of value in the data
# as you can see the various column have various spread
# we need to normalise the column so that column with good spread don't dominate the column
# with less spread
# normalisation is done using the z-score
# but we don't need to normalise the target variable, aka, price
normalized_listings = (dc_listings-dc_listings.mean())/dc_listings.std()
normalized_listings['price'] = dc_listings['price']

# find the eucleadian distance between accomodation and bathrooms
first_listing = [-0.596544, -0.439151]
second_listing = [-0.596544, 0.412923]
dist = distance.euclidean(first_listing, second_listing)

# find euclidean distance
first_fifth_distance = distance.euclidean(normalized_listings[0:5]['accommodates'], 
                                          normalized_listings[0:5]['bathrooms']) 


# use scikit learning library
train_df = normalized_listings.iloc[0:2792]
test_df = normalized_listings.iloc[2792:]
knn = KNeighborsRegressor(algorithm='brute')
knn = KNeighborsRegressor(algorithm='brute', n_neighbors=5)
knn.fit(train_df[['accommodates', 'bathrooms']], train_df['price'])
predictions = knn.predict(test_df[['accommodates', 'bathrooms']])
two_features_mse = mean_squared_error(test_df['price'], predictions)
two_features_rmse = two_features_mse ** (1/2)
# making model with more variable
features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')
knn.fit(train_df[features], train_df['price'])
four_predictions = knn.predict(test_df[features])
four_mse = mean_squared_error(test_df['price'], four_predictions)
four_rmse = four_mse**0.5
# using all features
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute')

features = train_df.columns.tolist()
features.remove('price')

knn.fit(train_df[features], train_df['price'])
all_features_predictions = knn.predict(test_df[features])
all_features_mse = mean_squared_error(test_df['price'], all_features_predictions)
all_features_rmse = all_features_mse ** (1/2)