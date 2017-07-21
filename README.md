# Simple Item Based Movie Recommender
Simple Item Based Movie Recommender 

This Recommender is based on Movie Lens 1M Dataset. [Get it here](https://grouplens.org/datasets/movielens/1m/)

### Data preparation instructions:

When you have downloaded data, here are a several things to fix:

#### Users DataFrame
- Users DataFrame should have columns: `user_id`, `gender`, `age`.
- Users should be saved at `[projectRoot]/data/users.csv`.

#### Movies DataFrame
- Since movies were mostly entered by hand, there were many errors and inconsistencies. Should be fixed by hand.
- Movies should be saved at `[projectRoot]/data/movies.csv`.

#### Ratings DataFrame
- Ratings DataFrame should have columns: `user_id`, `movie_id`, `rating`.
- Ratings should be saved `[projectRoot]/data/ratings.csv`.
