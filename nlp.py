import pandas as pd
submissions = pd.read_csv("D:/Study/Dataquest/Data sets/sel_hn_stories.csv", sep=',', names = ["submission_time", "upvotes", "url", "headline"])

# look into the data
submissions.info()
submissions.isnull().sum() # 189 null we can remove
submissions.dropna(inplace=True)

# using bag of words algorithm(model)
# step 1: tokenization
# =============================================================================
# print(submissions.iloc[0, 3].split(" "))
# tokenized_headlines = []
# for _ in range(0, submissions.shape[0]):
#     tokenized_headlines.append(submissions.iloc[_, 3].split(" "))
#     
# # trailing whitespace is coming in the data
# submissions['headline'] = submissions['headline'].str.strip()
# # in middle also some extra whitespace is coming
# import re
# #re.sub('\s+', ' ', mystring).strip()
# submissions['headline'] = submissions['headline'].str.replace('\s+','\s', regex=True )
# 
# 
# tokenized_headlines = []
# for _ in range(0, submissions.shape[0]):
#     tokenized_headlines.append(submissions.iloc[_, 3].split(" "))
# =============================================================================

tokenized_headlines = []
for item in submissions["headline"]:
    tokenized_headlines.append(item.split())

# step 2: clean the token -- convert into lower case and remove special characters
punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
clean_tokenized = []
for item in tokenized_headlines:
    tokens = []
    for token in item:
        token = token.lower()
        for punc in punctuation:
            token = token.replace(punc, "")
        tokens.append(token)
    clean_tokenized.append(tokens)
    
# step 3: make matrix of all unique words
import numpy as np
unique_tokens = []
single_tokens = []

token = []
for row in clean_tokenized:
    for element in row:
        token.append(element)
        
single_tokens = list(set(token))

for element in single_tokens:
    if token.count(element) > 1:
        unique_tokens.append(element)

# making matrix
import pandas as pd
counts = pd.DataFrame(0, index=np.arange(len(clean_tokenized)), columns=unique_tokens)

# We've already loaded in clean_tokenized and counts
for i, j in enumerate(unique_tokens):
    for k, row in enumerate(clean_tokenized):
        if j in row:
            counts.iloc[k, i] += row.count(j)
            
'''
There are two kinds of features that will reduce prediction accuracy. Features that occur only a few times will cause overfitting, because the model doesn't have enough information to accurately decide whether they're important. These features will probably correlate differently with upvotes in the test set and the training set.

Features that occur too many times can also cause issues. These are words like and and to, which occur in nearly every headline. These words don't add any information, because they don't necessarily correlate with upvotes. These types of words are sometimes called stopwords.
'''

# find the sum of each columns
# =============================================================================
# word_counts = []
# for col in counts:
#     word_counts.append(counts[col].sum())
# 
# selected_column = [0]*len(word_counts)
# for i, j in enumerate(word_counts):
#     if 5 <= j <=100:
#         selected_column[i] = 1
# =============================================================================
# find the sum of each columns       
word_counts = counts.sum(axis=0)
counts = counts.loc[:,(word_counts >= 5) & (word_counts <= 100)]


# splitting the data in train test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(counts, submissions['upvotes'], test_size=0.2, random_state=1)

# train
from sklearn.linear_model import LinearRegression
clf = LinearRegression()
clf.fit(X_train, y_train)
predict = clf.predict(X_test)