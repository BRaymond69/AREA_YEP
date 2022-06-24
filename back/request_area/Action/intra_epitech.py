#!/usr/bin/python3

import sys
import json
import requests
import urllib
import re
from datetime import datetime
from urllib.error import URLError, HTTPError
from datetime import date 


""" 
    For this service the programme need : nothing (maybe your own intra token)
    You got result of request inside dict here : info
    You can encore it in json and do what you want with this
"""

class Intra():
    def __init__(self, authToken):
        self.token = authToken
        self.info = {}
    
    def getNotification(self, old):
        url = "https://intra.epitech.eu/" + self.token + "/?format=json"
        try:
            response = urllib.request.urlopen(url)
        except:
            print("#######################################")
            return(84)
        data = json.loads(response.read())
        sums = []
        for i in range(len(data['current'])):
            sums.append(data['current'][i]['grade'])
        y = len(sums)
        self.info = {'Grade A' : str(round(sums.count('A') / y * 100, 1)),
                      'Grade B' : str(round(sums.count('B') / y * 100, 1)),
                      'Grade C' : str(round(sums.count('C') / y * 100, 1)),
                      'Grade D' : str(round(sums.count('D') / y * 100, 1)),
                      'Grade E' : str(round(sums.count('Echec') / y * 100, 1)),
                      'Grade -' : str(round(sums.count('-') / y * 100, 1)),
                      'Acquis'  : str(round(sums.count('Acquis') / y * 100, 1)),
                      }
        title = data['history'][old]['title']
        clean = re.compile('<.*?>')
        title = re.sub(clean, '', title)
        date_notif = data['history'][old]['date']
        date_notif = datetime.strptime(date_notif, '%Y-%m-%d %H:%M:%S')
        todays_date = datetime.today()
        difference_time = str(todays_date - date_notif).split(".")[0]
        self.info['Last notif'] = title
        self.info['since'] = difference_time
        return(self.info)

def main():
    try:
        info = Intra("auth-3b3d7ab8e40f1bbd90bf6aadd27b17fb7354f540").getNotification(0)
        print(info)
    except BaseException as error:
            sys.stderr.write(str(type(error).__name__) + ": {}\n".format(error))

if __name__ == "__main__":
    main()