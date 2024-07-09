import pandas as pd 
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer
from sklearn.model_selection import train_test_split


r_df = pd.read_csv('data/ratings.csv')
m_df = pd.read_csv('data/movies.csv')
t_df = pd.read_csv('data/tags.csv')

df = pd.merge(r_df, m_df[['movieId', 'genres']], on = 'movieId', how = 'left')

user_encoder = LabelEncoder()
movie_encoder = LabelEncoder()
mlb = MultiLabelBinarizer()

df['userId'] = user_encoder.fit_transform(df['userId'])
df['movieId'] = movie_encoder.fit_transform(df['movieId'])

df = df.join(pd.DataFrame(mlb.fit_transform(df.pop('genres').str.split('|')), columns = mlb.classes_, index = df.index ))