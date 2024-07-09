import argparse 
from backend.recs import get_recs
from backend.load import m_df 

def main(): 
 parser = argparse.ArgumentParser(description="Fetch movie recommendations for a user.")
 parser.add_argument("user_id", type=int, help="The ID of the user to fetch recommendations for")

 args = parser.parse_args()
 user_id = args.user_id

 recommendations = get_recs(user_id)
 top_n_movies_titles = m_df[m_df['movieId'].isin(recommendations)]['title'].tolist()
 print(f"Top 10 Recommendations for User {user_id}:")
 for i, title in enumerate(top_n_movies_titles, 1):
  print(f"{i}.{title}")

if __name__ == "__main__":
 main()

