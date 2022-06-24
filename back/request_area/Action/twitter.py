#!/usr/bin/python3

import requests
import sys
import json
import os


"""
Needed : Nothing
How program works : Need a name of username or account and it return the last tweet from this guys
"""

class Twitter():
    def __init__(self, source="SpaceX"):
        self.info = {}
        self.api_key = "uOqKfFeAD6lZVyra4dlNUSJib"
        self.api_secret_api = "reUIqFgZ0rqPd6K3xqN49WNHi2LU4bXOvYS8GvYnxthvhBng1x"
        self.source = source

    def auth(self):
        return "AAAAAAAAAAAAAAAAAAAAAFP8NAEAAAAABOsRqDBZsFWY%2BsHUAtPwsRoq%2BR0%3DstxEiipD1TcUnxBaXwiQ6DfOw17JBa6JoucjgL2iUn0wKHwAd6"

    def create_url(self):
        query = "from:" + self.source
        tweet_fields = "tweet.fields=author_id"
        url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
            query, tweet_fields
        )
        return url

    def create_headers(self, bearer_token):
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
        return headers


    def connect_to_endpoint(self, url, headers):
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            return(84)
        return response.json()
    
    def start(self):
        bearer_token = self.auth()
        url = self.create_url()
        headers = self.create_headers(bearer_token)
        json_response = self.connect_to_endpoint(url, headers)
        if json_response['meta']['result_count'] == 0:
            return(84)
        return(self.parsing(json.dumps(json_response)))
    
    def parsing(self, data):
        data = json.loads(data)
        response_data = data['data'][0]
        id_ = response_data['id']
        author_id = response_data['author_id']
        text = response_data['text']
        self.info = {
            "Author": author_id,
            "Id": id_,
            "Text" : text
        }
        return self.info

def main():
    try:
        info = Twitter("G2kennyS").start()
        print(info)
    except BaseException as error:
        sys.stderr.write(str(type(error).__name__) + ": {}\n".format(error))
if __name__ == "__main__":
    main()
    