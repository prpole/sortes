#!/usr/bin/python

import sys

import tweepy,sys,time,random
from nltk.tokenize import RegexpTokenizer

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'BvkxtoSU9qNK4s3nncattaRZM'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'uZLIQ6C0PmMGwLHuO5mIhlFUMKeoTUHBmsfnqLKEviKwazsKVw'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '615528592-FuZIIFycOEmyNaEUtSMXpJ5iyPZSEqK5Oz4I7GoN'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'Ospy8ZPsgNPkUWhbuG8DsjNVfLwZZXYG1RjKSYD7Ob9Eh'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#init tokenizer
tokenizer = RegexpTokenizer(r'[\'\w\-]+[.,\'"!?;/]*')


with open('/home/phlip/sortes/aeneid.txt','r') as f:
	text = f.read()

words = tokenizer.tokenize(text)

start = random.randint(0,len(words)-20)

message = []

for ndx,i in enumerate(words[start:]):
		if sum([len(n) for n in message])+len(words[ndx]) < 90:
			message.append(i)

message = ' '.join(message)

while len(message)>140:
	for ndx,i in enumerate(words[start:]):
		if sum([len(n) for n in message])+len(words[ndx]) < 90:
			message.append(i)

	message = ' '.join(message)

print message
api.update_status(status=message+' #SortesVergilianae')
