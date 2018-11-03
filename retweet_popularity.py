import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter

CONSUMER_KEY = 'WzT76mRT2z1oACipf0Fa6w5fP'
CONSUMER_SECRET = 'u0Ni4LVE4O1qhWgYfWIagMG8gcnI7arJJm8b2v56cFSW94LMRA'
OAUTH_TOKEN = '272497238-hnCGnwFeU9xhVWlTd9AKy1gyIk6QF5Egtm9AI8Bm'
OAUTH_TOKEN_SECRET = 'x4ZPGXwRWbKfId48uzxuSmG4BzwYLzNAmpIEijRSDq1fi'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Invoke tweepy API and pass auth token
api = tweepy.API(auth)

count = 150
query = 'Ireland'

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10 # Min number of retweets to gain entry to the list
                  # change this value to suit your needs

pop_tweets = [status
              for status in results
                  if status._json['retweet_count'] > min_retweets]

# Create list of tweet tuples associating each tweet text with its retweet count
tweet_tups = [(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count'])
              for tweet in pop_tweets]

# Sort the tuple entries in descending order
most_popular_tups = sorted(tweet_tups, key=itemgetter(1), reverse=True)[:5]

#prettify
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in most_popular_tups:
    table.add_row([key, val])
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = 'l', 'r' #align the columns
print(table)