#!/usr/bin/python3

import sys
from bs4 import BeautifulSoup
import requests
import re
from datetime import date
import datetime


class Netflix():
    def __init__(self):
        self.url = "https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-this-week-march-1st-to-7th-2021/"
        self.date = date.today()

    def start(self, number="last"):
        response = requests.get(self.url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            div = soup.find_all("div", {"class": "entry-inner"})
            headers = [elem.find_all("li") for elem in div]
            headers = self.clear(str(headers))
            headers = headers.replace("starring", "with").split(",")
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
        info = Netflix().start("all")
        print(info)
    except BaseException as error:
        sys.stderr.write(str(type(error).__name__) + ": {}\n".format(error))

if __name__ == "__main__":
    main()