# things we need from libraries
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

# variables for OAuth
consumer_key =  "GqJ0To5CvesWU1TiYVm2exnFt"
consumer_secret = "JYko8VKYMXxYEZqiN5ubDcp4Cvyb09JDyGQ2yngdvjjqHbBytf"

access_token = "38770826-0J9bCkMuQwjAjyQIteozK5pRfwBqmZgZ3W20PasaJ"
access_token_secret = "aLrYZugrIseyyv85tvtXSfUs17Gzp2d8EEQbYOI2GeunA"

class Listener(StreamListener):

    tweetCount = 0
    stopAt = 1000 # default set to crawl 1000 tweets
    file2writeto = ""

    def login(self):
        # handles authentication
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth 
    
    def on_exception(self, exception):
        print exception
        return False

    def on_data(self, data):

        #increment how many tweets have been crawled
        Listener.tweetCount += 1

        # open file to write to in append mode
        ofile = open(Listener.file2writeto, 'a')
        ofile.write(data)
        ofile.close()

        if Listener.tweetCount < Listener.stopAt:
            return True
        else:
            print "max tweets reached"
            return False

    def on_error(self, status):
        if status == 420:
            print "status 420, disconnecting stream"
            # disconnecting the stream
            return False

    def getTweetsByKeyword(self, numTweets2Stop):
        # get tweets that contain these keywords from command line args
        if len(sys.argv) < 3:
            print "cannot open stream, not enough arguments to track"
    
        else:
            # set file to output to
            Listener.file2writeto = sys.argv[1]

            # set number of tweets to crawl
            Listener.stopAt = numTweets2Stop
            
            # login to the stream
            auth = self.login()

             # opens the stream and keeps it alive for 60s after receiving no data 
            stream = Stream(auth, Listener(), timeout=60)
            
            # array to store terms to track in the stream
            # takes the terms from command line arguments
            terms2track = []
            for x in range(1, len(sys.argv)):
                 terms2track.append(sys.argv[x])
            
            # apply filter to stream to track only key words
            stream.filter(track=terms2track)
    
def main():
    # Initialize Listener object
    crawler = Listener()
    crawler.getTweetsByKeyword(10000000000)

if __name__ == "__main__":
    main()
