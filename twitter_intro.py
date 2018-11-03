import json
import tweepy
from tweepy import OAuthHandler
from twitter import get_auth, twitter_api

api = twitter_api()
auth = get_auth()

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