#!/usr/bin/python

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/')

import tweepy,sys,time,random
from nltk.tokenize import RegexpTokenizer

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'JPEnkkONKSl3oC4ssQFqE0uuU'#keep the quotes, replace this with your consumer keyBvkxtoSU9qNK4s3nncattaRZM CONSUMER_SECRET = 'uZLIQ6C0PmMGwLHuO5mIhlFUMKeoTUHBmsfnqLKEviKwazsKVw'#keep the quotes, replace this with your consumer secret key
CONSUMER_SECRET = 'Qgi45KKskXVQCZZ96GUK1YeZb2uJGmHhqJqHyUQiu1Gw4ex4Rr'
ACCESS_KEY = '615528592-Z2vZXXhsxO0rRxJ531nyoW3G2CX0nYUm9GHkQdut'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'TARwszwh3ORvTKgcNSHJSximrJDkOiBgFPpYQIH3m47RH'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#init tokenizer
tokenizer = RegexpTokenizer(r'[^\s]+')


with open('/Users/phillippolefrone/git/sortes/gravitys_rainbow.md','r') as f:
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
api.update_status(status=message+' #SortesPynchonianae')
