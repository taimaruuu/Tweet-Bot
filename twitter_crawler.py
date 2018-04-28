# things we need from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# variables for OAuth
consumer_key =  "GqJ0To5CvesWU1TiYVm2exnFt"
consumer_secret = "JYko8VKYMXxYEZqiN5ubDcp4Cvyb09JDyGQ2yngdvjjqHbBytf"

access_token = "38770826-0J9bCkMuQwjAjyQIteozK5pRfwBqmZgZ3W20PasaJ"
access_token_secret = "aLrYZugrIseyyv85tvtXSfUs17Gzp2d8EEQbYOI2GeunA"

class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)

    # get tweets that contain these keywords
    stream.filter(track=['fortnite', 'kanye', 'trump', 'new', 'gaming', 'iphone', 'mac', 'fashion'])
