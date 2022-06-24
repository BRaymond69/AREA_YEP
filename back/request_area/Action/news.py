#!/usr/bin/python3
import requests
import os
import sys
import json
from datetime import datetime
from datetime import date
from datetime import timedelta

""" 
    For this service the programme need key_word for research like : FootBall, Corona Virus, Joe Biden
    You got result of request inside dict here : info
    You can encore it in json and do what you want with this
    Be carefull you get onyl 500 request per months !!
"""

class News():
    def __init__(self):
        self.token =  "08a270bca5b2f11c7f94d38848655835"
        self.key_word = ""
        self.newspapper = ""
        self.info = {}
        self.return_data = []
        self.list_categorie = ['business', 'entertainment', 'health', 'science', 'sports', 'technology']
        self.date = date.today()
        self.date_request = self.date-timedelta(days=31)

    def start(self, key_word = "Tesla", limit = 3):
        self.key_word = key_word
        if len(key_word) == 0:
            self.key_word = "Mars Rover"
        self.newspapper = "cnn, bbc, nytimes, time, cbs"
        if int(limit) == 0:
            limit = 5
        response = requests.get(
            "http://api.mediastack.com/v1/news?access_key="+self.token+"&keywords="+self.key_word+"&limit="+str(limit)+"&sources="+self.newspapper
            )
        if response.status_code != 200:
            return(84)
        response = json.loads(response.text)
        if len(response['data']) == 0:
            return 84
        return(self.parsing(response, limit))
        
    def parsing(self, data, limit):
        brain = ""
        for i in range(0, limit):
            brain = data['data'][i]
            publish = (brain['published_at'].split('T')[0]) + " " +(brain['published_at'].split('T')[1].split("+")[0])
            timing = datetime.strptime(publish, '%Y-%m-%d %H:%M:%S')
            since = datetime.now() - timing
            days = (str(since).split("days")[0])
            if int(days) >= 14:
                recent = False
            else:
                recent = True
            self.info = {
                "Source": brain['source'],
                "Title": brain['title'],
                "Description": brain['description'],
                "Redirect_url": brain['url'],
                'Category': brain['category'],
                'Publish since' : str(since),
                'Recent' : recent #return True or False if the article is older than 7 days
            }
            self.return_data.append(self.info)
        return(self.return_data)

def main():
    try:
        info = News().start() #take research word + number of article
        # print(info)
    except BaseException as error:
        sys.stderr.write(str(type(error).__name__) + ": {}\n".format(error))

if __name__ == "__main__":
    main()
