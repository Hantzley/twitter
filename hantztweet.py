#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Author: Hantzley Tauckoor
Date: 1 July 2017
Version: 1
Description: Sample script to access Twitter API
'''
import json
import oauth2 as oauth
from tokens import Consumer_Key, Consumer_Secret, Access_Token, Access_Token_Secret

consumer = oauth.Consumer(key=Consumer_Key,secret=Consumer_Secret)
Oauth_Access_Token = oauth.Token(key=Access_Token, secret=Access_Token_Secret)
client = oauth.Client(consumer, Oauth_Access_Token)

timeline_endpoint = 'https://api.twitter.com/1.1/statuses/home_timeline.json'

response, data = client.request(timeline_endpoint)

tweets = json.loads(data)

for tweet in tweets:
    print ("\n\n" + json.dumps(tweet, indent=4))
