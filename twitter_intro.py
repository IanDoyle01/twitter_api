import json
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

# Yahoo Where on Earth ID for Dublin
DUB_WOE_ID = 560743
LON_WOE_ID = 44418
NIR_WOE_ID = 44544

# Invoke trends place api from tweety and pass location
dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)
nir_trends = api.trends_place(NIR_WOE_ID)

# create sets for trends
# Dublin
dub_trends_set = set([trend['name']
                     for trend in dub_trends[0]['trends']])
# London                     
lon_trends_set = set([trend['name']
                     for trend in lon_trends[0]['trends']])
# Northern Ireland
nir_trends_set = set([trend['name']
                     for trend in nir_trends[0]['trends']])

# find intersecting trends for Dublin, London and Northen Ireland
common_trends = set.intersection(dub_trends_set, lon_trends_set, nir_trends_set)

print(common_trends)