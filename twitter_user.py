import tweepy
from tweepy import OAuthHandler
from twitter import get_auth, twitter_api

api = twitter_api()
auth = get_auth()

# Invoke tweepy API and pass auth token
api = tweepy.API(auth)

# Print the 10 most recent tweets by people followed by account
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a tweet
    print(status.text)