#!/usr/bin/python3
import datetime
import os
import sys


""" 
    For this service the programme need a day of the week
    You got result of request inside dict here : info
    You can encore it in json and do what you want with this
"""

class Date() :
    def __init__(self):
        self.weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        self.today_date = ""

    def start(self, day):
        if len(day) == 0:
            day = "Sunday"
        if day not in self.weekDays:
            return(84)
        x = datetime.datetime.now()
        self.today_date = x.strftime("%A")
        if self.today_date in self.weekDays:
            index = self.weekDays.index(self.today_date)
            index_futur_day = self.weekDays.index(day)
            result = index_futur_day - index
            if result < 0:
                result = 7 + result
                value = "It's will be", day, "in", result, "days"
                return({value})
            if result == 0:
                return ({"Same day"})
            else:
                value = "It's will be", day, "in", result, "days"
                return({value})

        else:
            return ({"Error"})

def main():
    try:
        # day = "" #Should be a input
        info = Date().start("")
        # print(info)
    except BaseException as error:
        sys.stderr.write(str(type(error).__name__) + ": {}\n".format(error))



if __name__ == '__main__':
    main()