import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable

CONSUMER_KEY = 'WzT76mRT2z1oACipf0Fa6w5fP'
CONSUMER_SECRET = 'u0Ni4LVE4O1qhWgYfWIagMG8gcnI7arJJm8b2v56cFSW94LMRA'
OAUTH_TOKEN = '272497238-hnCGnwFeU9xhVWlTd9AKy1gyIk6QF5Egtm9AI8Bm'
OAUTH_TOKEN_SECRET = 'x4ZPGXwRWbKfId48uzxuSmG4BzwYLzNAmpIEijRSDq1fi'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Invoke tweepy API and pass auth token
api = tweepy.API(auth)

count = 50
query = 'Weather'

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [status._json['text'] for status in results]

screen_names = [status._json['user']['screen_name'] 
                for status in results
                   for mention in status._json['entities']['user_mentions'] ]

hashtags = [hashtag['text']
                for status in results
                    for hashtag in status._json['entities']['hashtags'] ]

words = [ word 
                for text in status_texts
                    for word in text.split() ]

for label, data in (('Text', status_texts),
                    ('Screen Name', screen_names),
                    ('Word', words)):
        table = PrettyTable(field_names=[label, 'Count'])
        counter = Counter(data)
        [table.add_row(entry) for entry in counter.most_common()[:10]]
        table.align[label], table.align['Count'] = 'l', 'r' #align the columns
        print(table)