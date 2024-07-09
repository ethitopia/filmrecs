from surprise import Dataset, Reader
from surprise.prediction_algorithms.matrix_factorization import SVD
from surprise import accuracy 
from .load import df 
from sklearn.model_selection import train_test_split
import pandas as pd 


train_df, test_df = train_test_split(df, test_size = 0.2)

reader = Reader(rating_scale = (0.5, 5))
data = Dataset.load_from_df(train_df[['userId', 'movieId', 'rating']], reader)
trainset = data.build_full_trainset()

model_svd = SVD()
model_svd.fit(trainset)

predictions_svd = model_svd.test(trainset.build_anti_testset())
accuracy.rmse(predictions_svd)