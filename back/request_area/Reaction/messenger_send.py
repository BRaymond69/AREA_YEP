#!/usr/bin/python3

import fbchat
import sys
from getpass import getpass 


"""
    Needed : fbchat -> pip3 install fbchat
    For this service the programme need your email and password for facebook connection
    Need your own message, and the name of recipient friend
"""
   
class Facebook_Sender():
    def __init__(self, username = "", password = "", msg = "Hello Mec, ne fait pas attetion au message c est le test de mon API", friendname = ""):
        self.username = username
        self.password = password
        self.msg = msg
        self.friendname = friendname
    
    def start(self):
        try:
            client = fbchat.Client(self.username, self.password, max_tries=2)
        except:
            return(84)
        friends = client.searchForUsers(self.friendname)
        friend = friends[0]
        client.sendMessage(self.msg, thread_id=friend.uid)
    

def main():
    try:
        Facebook_Sender().start()
    except BaseException as error:
        sys.stderr.write(str(type(error).__name__) + ": {}\n".format(error))

if __name__ == "__main__":
    main()