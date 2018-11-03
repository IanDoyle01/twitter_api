import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'WzT76mRT2z1oACipf0Fa6w5fP'
CONSUMER_SECRET = 'u0Ni4LVE4O1qhWgYfWIagMG8gcnI7arJJm8b2v56cFSW94LMRA'
OAUTH_TOKEN = '272497238-hnCGnwFeU9xhVWlTd9AKy1gyIk6QF5Egtm9AI8Bm'
OAUTH_TOKEN_SECRET = 'x4ZPGXwRWbKfId48uzxuSmG4BzwYLzNAmpIEijRSDq1fi'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Invoke tweepy API and pass auth token
api = tweepy.API(auth)

# Print the 10 most recent tweets by people followed by account
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a tweet
    print(status.text)