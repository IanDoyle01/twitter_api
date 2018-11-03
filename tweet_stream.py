from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

CONSUMER_KEY = 'WzT76mRT2z1oACipf0Fa6w5fP'
CONSUMER_SECRET = 'u0Ni4LVE4O1qhWgYfWIagMG8gcnI7arJJm8b2v56cFSW94LMRA'
OAUTH_TOKEN = '272497238-hnCGnwFeU9xhVWlTd9AKy1gyIk6QF5Egtm9AI8Bm'
OAUTH_TOKEN_SECRET = 'x4ZPGXwRWbKfId48uzxuSmG4BzwYLzNAmpIEijRSDq1fi'

keyword_list = ['python', 'javascript', 'php', 'C#'] # track list

limit = 500

# Extend StreamListener
class MyStreamListener(StreamListener):
    
    def __init__(self):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
    
    def on_data(self, data):
        # limit to 500 results
        if self.num_tweets < limit:
            self.num_tweets += 1
            try:
                with open('tweet_mining.json', 'a') as tweet_file:
                    tweet_file.write(data)
                    return True
            except BaseException as e:
                print("Failed on_data: %s"%str(e))
            return True
        else:
            return False
    
    def on_error(self, status):
        print(status)
        return True

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Create an instance of the stream class
twitter_stream = Stream(auth, MyStreamListener())
# Filter by the keyword list
twitter_stream.filter(track=keyword_list)