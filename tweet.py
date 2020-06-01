import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user =api.me()

def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)

search_string =''#name you want to give a like, and to retweet
numberofTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberofTweets):
	try:
		tweet.favorite()
		tweet.retweet()
		print('i liked that tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break
