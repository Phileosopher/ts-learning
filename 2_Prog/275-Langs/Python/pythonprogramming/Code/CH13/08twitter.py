import tweepy
import json

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'your consumer key'
consumer_secret = 'your secret key'
access_token = 'your access token
access_token_secret = 'your secret token'

# This is the listener, responsible for receiving data
class tweet_listener(tweepy.StreamListener):
    def on_data(self, data):
        dict = json.loads(data)
        print (dict['user']['location'])
        print (dict['user']['screen_name'], dict['text'])
        return True

    def on_error(self, status):
        print (status)

authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_token_secret)
listener = tweet_listener()

print ("Showing all new tweets for #startrek:")

stream = tweepy.Stream(authentication, listener)
print (stream)
stream.filter(track=['Star Trek'])