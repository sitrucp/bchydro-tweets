import tweepy
#import MySQLdb
from datetime import datetime
import random
import sys, os
import json
from dateutil import tz
from tweet_auth import *

#get twitter auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#bch_tweets = list()

def main():
	with open('bchtweets.csv', 'wb') as file:
		for status in tweepy.Cursor(api.user_timeline, id='bchydro').items(1800):
			file.write(str(status.created_at.replace(tzinfo=tz.gettz('UTC')).astimezone(tz.gettz('America/Los_Angeles')).replace(tzinfo=None)) + ', ' + status.text.encode('utf8') + '\n')

if __name__ == '__main__':
	main()
