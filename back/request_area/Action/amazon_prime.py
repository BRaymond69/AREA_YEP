#!/usr/bin/python3

import sys
from bs4 import BeautifulSoup
import requests
import re
from datetime import date
import datetime


class Amazon_video():
    def __init__(self):
        self.url = "https://decider.com/article/new-on-amazon-prime/"
        self.date = date.today()

    def start(self, number="last"):
        response = requests.get(self.url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            div = soup.find_all("div", {"class": "entry-content-read-more"})
            headers = [elem.find_all("i") for elem in div]
            headers = self.clear(str(headers))
            headers = headers.split(",")
            headers[0] = headers[0][2:]
            headers[len(headers) -1] = headers[len(headers) -1][:-2]
            if number == "last":
                return(headers[0])
            if number == "all":
                return(headers)
            else:
                return(84)

    def clear(self, data):
        clean = re.compile('<.*?>')
        data = re.sub(clean, '', data)
        return(data)

def main():
    try:
        Amazon_video().start()
        # print(info)
    except BaseException as error:
        sys.stderr.write(str(type(error).__name__) + ": {}\n".format(error))

if __name__ == "__main__":
    main()