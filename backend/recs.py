
from .load import movie_encoder 
from .model import model


def get_recs(df, user_id, n=10):
  user_movies = df[df['userId'] == user_id]['movieId'].unique()
  all_movies = df['movieId'].unique()
  movies_predict = list(set(all_movies) - set(user_movies))

  user_movie_pairs = [(user_id, movie_id, 0) for movie_id in movies_predict]
  predictions_cf = model.test(user_movie_pairs)

  top_n_recommendations = sorted(predictions_cf, key = lambda x: x.est)[:n]

  for pred in top_n_recommendations:
    predicted_rating = pred.est
    print(predicted_rating)

  top_n_movie_ids = [int(pred.iid) for pred in top_n_recommendations]

  top_n_movies = movie_encoder.inverse_transform(top_n_movie_ids)

  return top_n_movies 
