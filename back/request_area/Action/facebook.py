#!/usr/bin/python3
import fbchat
import sys
import getpass
from fbchat import Client
from datetime import datetime
from datetime import date


"""
    Mandatory: pip3 install fbchat
    You need to change setting in file /home/user/.local/lib/python3.7/site-packages/fbchat/_state.py" Line 190
    Change => revision = int(r.text.split('"client_revision":', 1)[1].split(",", 1)[0])
    to  => revision = 1 
    For this service the programme need your email and password for facebook connection
    You got result of request inside dict here : info
    You can encore it in json and do what you want with this
"""

class Facebook():
    def __init__(self, username="", password=""):
        self.username = username
        self.password = password
        self.info = {"ID" : 0,
                     "Url_Photo" : "",
                     "name" : "",
                     "timestamp" : 0,
                     "last_message": 0,
                    }
# login
    def modif_file(self):
        pythonV = sys.version[:3]
        the_wrong_str = "revision = int(r.text.split('\"client_revision\":', 1)[1].split(\",\", 1)[0])"
        username = getpass.getuser()
        fin = open("/home/"+username+"/.local/lib/python"+pythonV+"/site-packages/fbchat/_state.py", "rt")
        data = fin.read()
        data = data.replace(the_wrong_str, 'revision = 1')
        fin.close()
        fin = open("/home/"+username+"/.local/lib/python"+pythonV+"/site-packages/fbchat/_state.py", "wt")
        fin.write(data)
        fin.close()

    def start(self):
        # self.modif_file()
        try:
            client = Client(self.username, self.password, max_tries=2)
        except:
            return(84)
        users = client.fetchThreadList()
        return(users[1::2])

    def parsing(self, data):
        if data == 84:
            return(84)
        spliter = str(data).split("(")
        spliter.remove(spliter[0])
        new_data = list(spliter[0].split(", "))
        self.info["ID"] = int(new_data[0].split("=")[1].replace("'", ""))
        self.info["Url_Photo"] = new_data[2]
        self.info["name"] = new_data[3].split("=")[1].replace("'", "")
        self.info["timestamp"] = int(new_data[4].split("=")[1].replace("'", "")[:10])
        todays_date = datetime.today()
        dt_object = datetime.fromtimestamp(self.info["timestamp"])
        c = todays_date - dt_object
        self.info["last_message"] = "Last message reiceive since " + str(c).split(".")[0]
        return(self.info)
        

def main():
    try:
            coo = Facebook()
            data = coo.start()
            info = coo.parsing(data)
        # print(info)
    except BaseException as error:
        sys.stderr.write(str(type(error).__name__) + ": {}\n".format(error))
        
if __name__ == "__main__":
    main()