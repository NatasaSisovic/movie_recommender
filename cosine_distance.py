
import pandas as pd
from scipy.spatial.distance import cosine

ratings_columns = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('./data/ratings.csv', sep=',', names=ratings_columns, encoding='latin-1')

movies_columns = ['movie_id', 'title', 'genres']
movies = pd.read_csv('./data/movies.csv', sep=',', names=movies_columns, encoding='latin-1')

movies_ratings = pd.merge(movies, ratings)

movies_ratings = movies_ratings.pivot_table(index=['user_id'],columns=['title'],values='rating',aggfunc=lambda x: len(x.unique()),fill_value=0)

movies_ratings.reset_index(inplace = True)

movies_ratings = movies_ratings.drop('user_id', axis = 1)

processed_cosine_ratings = pd.DataFrame(index=movies_ratings.columns,columns=movies_ratings.columns)

for i in range(0,len(processed_cosine_ratings.columns)):
  for j in range(0,len(processed_cosine_ratings.columns)):
    processed_cosine_ratings.ix[i,j] = 1-cosine(movies_ratings.ix[:,i],movies_ratings.ix[:,j])

processed_cosine_ratings.to_csv("./data/final.csv")
