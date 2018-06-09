# Twitter Crawler

Our crawler uses the streaming API to crawl tweets based on keywords given by the user.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

Upgrade pip

```
pip install --upgrade pip
```
Install tweepy
```
pip install tweepy
```

### Installing

Make sure you have the prerequisites

1. Clone github repository

```
git clone https://github.com/taimaruuu/cs172.git
```

## Running the crawler

To run this crawler you need at least 2 arguments, the ouput file and one keyword to track.
For example:
```
python twitter_crawler.py output.txt word
```
The above command will write output to output.txt and look for 'word' in tweets to write to that file.

### Modifying the crawler

If you would like to change the number of tweets to crawl, you have to change the number in the getTweetsByKeyword() function call in main().
For example:
```
crawler.getTweetsByKeyword(100)
```
The above command will crawl 100 tweets before closing the stream.

## Commands used to get the tweets in this repository

* trump.txt
```
python twitter_crawler.py tweets/trump8.txt trump president maga potus
```

* avengers.txt
```
python twitter_crawler.py tweets/avengers.txt infinity war avengers marvel dc iron man spider man batman movies premiere
```

* shoes.txt
```
python twitter_crawler.py tweets/shoes.txt yeezy adidas nike ultra boost air max converse off white jordan
```

* fortnite.txt
```
python twitter_crawler.py tweets/fortnite.txt fornite epicgames new skin season 4
```

* kanye.txt
```
python twitter_crawler.py tweets/kanye.txt kanye yeezy west kanyewest
```

* tech.txt
```
python twitter_crawler.py tweets/tech.txt apple microsoft iphone ipad macbook imac samsung tech technology
```

* nba.txt
``` 
python twitter_crawler.py tweets/nba.txt nba nba2k18 nba2kleague 2kleague nbaleague 
```

## Built With

* [Twitter Streaming API](https://developer.twitter.com/en/docs) - The API used
* [Tweepy](http://www.tweepy.org) - Python library for accessing the Twitter API.

## Authors

* **Taimaru Provensal** - [Github](https://github.com/taimaruuu)
* **Arav Batra** - [Github](https://github.com/aravbatra)

## License

This project is licensed under the BSD 3-Clause License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Stackoverflow
* [README template used](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
