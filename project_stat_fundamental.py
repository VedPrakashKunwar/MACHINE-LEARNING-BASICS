# import module
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import arange

pd.options.display.max_rows = 200
pd.options.display.max_columns = 50

# import dataset
before = pd.read_csv('D:/Study/Dataquest/Data Sets/fandango_score_comparison.csv')
after = pd.read_csv('D:/Study/Dataquest/Data Sets/movie_ratings_16_17.csv')
# inspecting the data
df_before = before[['FILM', 'Fandango_Stars', 'Fandango_Ratingvalue', 'Fandango_votes', 'Fandango_Difference']]
df_after = after[['movie', 'year', 'fandango']]