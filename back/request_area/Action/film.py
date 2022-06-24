#!/usr/bin/python3

import sys
from bs4 import BeautifulSoup
import requests
import re
import dateparser
from datetime import date
import datetime



class Film():
    def __init__(self):
        self.url = "https://www.cinehorizons.net/film/2021"
        self.date = date.today()
        self.info = {
                    "Film" : "",
                    "Date sortie": "",
                    "J-" : 0,
                    }

    def start(self, number = 14):
        response = requests.get(self.url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            div = soup.findAll({'h3' :'itemprop=\"name\"'})
            film_data = self.clear(str(div)).split(',')
            film_data[0] = film_data[0][1:]
            film_data[len(film_data) -1] = film_data[len(film_data) -1][:-1]
            div_date = soup.findAll('span', {'class': 'date-sortie'})
            hour_data = self.clear(str(div_date)).split(',')
            hour_data[0] = hour_data[0][1:]
            hour_data[len(hour_data) -1] = hour_data[len(hour_data) -1][:-1]
            new_date, tmp_film, tmp_hour, tmp_J = [], [], [], []
            for date_string in hour_data:
                new_date.append((dateparser.parse(date_string).date()))
            for i in range(len(new_date)): 
                x = (new_date[i] - self.date)
                if new_date[i] > self.date:
                    if int(str(x).split()[0]) < int(number):
                        tmp_film.append(film_data[i])
                        tmp_hour.append(hour_data[i])
                        tmp_J.append(int(str(x).split()[0]))
                        self.info["Film"] = tmp_film
                        self.info["Date sortie"] = tmp_hour
                        self.info["J-"] = tmp_J
        return(self.info)

    def clear(self, data):
        clean = re.compile('<.*?>')
        data = re.sub(clean, '', data)
        return(data)

def main():
    try:
        info = Film().start("30")
        print(info)
    except BaseException as error:
        sys.stderr.write(str(type(error).__name__) + ": {}\n".format(error))

if __name__ == "__main__":
    main()