#!/usr/bin/python3

import requests
import sys
import json


""" 
    For this service the programme need a name of Twitch channel
    You got result of request inside dict here : info
    You can encore it in json and do what you want with this
    Be carefull you get onyl 100 request per days !!
    
"""

class Twitch():
    def __init__(self):
        self.channel = ""
        self.hearders = {}
        self.client_id = "6932z9ha8m0zhd9bu1ipm5cmkv1yke"
        self.client_secret = "gkalw6jvxhxakkdsu61wfakupyak3s"
        self.access_token = ""
        self.twitch_info = {}

    def start(self, channel = "Solary"):
        self.channel = channel
        if len(channel) == 0:
            self.channel = "Sididi"
        access_code = requests.post('https://id.twitch.tv/oauth2/token?client_id='+str(self.client_id)+'&client_secret='+str(self.client_secret)+'&grant_type=client_credentials')
        if access_code.status_code == 200:
            access_token = json.loads(access_code.text)
            self.access_token = access_token['access_token']
            self.headers = {
                'client-id' : str(self.client_id),
                'Authorization' : 'Bearer '+str(self.access_token),
            }
            response = requests.get('https://api.twitch.tv/helix/search/channels?query='+str(self.channel), headers=self.headers)
            if response.status_code != 200:
                raise Exception(response.status_code, response.text)
            response_json = json.loads(response.text)
            return(self.parsing(response_json))
        else:
            return(84)
    
    def parsing(self, data):
        for i in range(len(data['data'])):
            if data['data'][i]['display_name'] == self.channel:
                result = data['data'][i]
                if result['is_live'] == True:
                    id_game = result['game_id']
                    title = result['title']
                    url = result['thumbnail_url']
                    r = requests.get("https://api.twitch.tv/helix/games?id=" + id_game, headers=self.headers)
                    response = json.loads(r.text)
                    name_game = response['data'][0]['name']
                    self.twitch_info = { "Streamer": self.channel,
                                        "Start at": result['started_at'],
                                        "play": name_game,
                                        "is_live": True, 
                                        "live title": title,
                                        "url photo": url
                                        }
                    return(self.twitch_info)
            else:
                continue


def main():
    try:
        info = Twitch().start()
        print(info)
    except BaseException as error:
        sys.stderr.write(str(type(error).__name__) + ": {}\n".format(error))
        
if __name__ == "__main__":
    main()
    
