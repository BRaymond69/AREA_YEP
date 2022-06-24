#!/usr/bin/python3

import tweepy 
import sys

"""
Needed : pip3 install tweepy
How programm work : Need a sentence you want to send on twitter and that's it
"""

class Twitter_post():
    def __init__(self, consumer_key='uOqKfFeAD6lZVyra4dlNUSJib', consumer_secret='reUIqFgZ0rqPd6K3xqN49WNHi2LU4bXOvYS8GvYnxthvhBng1x',
    access_token = '882246392575610880-SFY3HIh3JmDV4ucoyRshcdJoprEwsP4', access_token_secret = 'TC23VoJ75ZsM7PIfD5eakXngIhSy3vzSXt9ndrM2qiZab'):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret 
        self.access_token = access_token 
        self.access_token_secret = access_token_secret

    def start(self, sentence = "Hello is my API TEST for AREA an Epitech Project"):
        try:
            auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
            auth.set_access_token(self.access_token, self.access_token_secret)
        except:
            return(84)
        api = tweepy.API(auth)
        api.update_status(sentence)
        
def main():
    try:
        Twitter_post().start()
    except BaseException as error:
        sys.stderr.write(str(type(error).__name__) + ": {}\n".format(error))
if __name__ == "__main__":
    main()