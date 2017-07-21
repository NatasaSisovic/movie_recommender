import pandas as pd

def load_movies():
  movies_columns = ['id', 'title', 'genres']
  movies = pd.read_csv('./data/movies.csv', sep=',', names=movies_columns, encoding='latin-1')
  return movies

def load_processed_cosine_distances():
  return pd.DataFrame.from_csv('./data/cosine_distances.csv', encoding='latin-1')

def get_movie(movies, movie_id):
  return movies.loc[movies['id'] == int(movie_id)]

def sort_by_rating(processed_dataset):
  sorted_movies = pd.DataFrame(index=processed_dataset.columns,columns=range(1,12))
  for i in range(0,len(processed_dataset.columns)): 
      sorted_movies.ix[i,:11] = processed_dataset.ix[0:,i].sort_values(ascending=False)[:11].index
  return sorted_movies

def get_similar_movies_for_movie(rating_sorted, movie_title):
  return rating_sorted.ix[movie_title, 2:12]

print('Welcome to simple Item-Based Movie Recommender based on MovieLens 1M dataset.')
print('You can exit at any time by using Ctrl-C.')
print('By Natasa Sisovic. Enjoy!')
print('')
print('Loading data please wait...')
print('')

movies = load_movies()
processed_dataset = load_processed_cosine_distances()
rating_sorted = sort_by_rating(processed_dataset)

while(True):
  movie_id = input('Specify movie_id to get similar movies for: ')

  movie = get_movie(movies, movie_id)
  
  if movie.empty:
    print('Movie does not exist. Try again.')
    continue
  else:
    print(movie)

  print('Top 10 movies are:')
  print('')

  print(get_similar_movies_for_movie(rating_sorted, movie.iloc[0]['title']))
  


