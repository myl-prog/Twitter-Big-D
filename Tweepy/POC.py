import os
from dotenv import load_dotenv
import tweepy

load_dotenv()

# Clés d'accès à l'API Twitter
consumer_key = os.getenv('API_Key')
consumer_secret = os.getenv('API_Key_Secret')
access_token = os.getenv('Access_Token')
access_token_secret = os.getenv('Access_Token_Secret')

# Authentification à l'API Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Récupération des informations d'un tweet à partir de son URL
#url = "https://twitter.com/<username>/status/<tweet_id>"
url = "https://twitter.com/TheGreatReview_/status/1613552566796980224"
status = api.get_status(url.split("/")[-1])
print(status.text)