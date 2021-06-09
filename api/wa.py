import json
import requests
import datetime

class WABot():
    def __init__(self):
        #self.json = json
        #self.dict_messages = json['messages']
        self.APIUrl = 'https://api.chat-api.com/instance270570/'
        self.token = 'u8qq8fn4rx98zij9'

    def send_requests(self, method, data):
        url = f"{self.APIUrl}{method}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    def send_message(self, chatId, token, phone):
        data = {"chatId" : chatId,
                "body" : "This is your token [ " + str(token) + " ]",
                "phone" : phone}
        answer = self.send_requests('sendMessage', data)
        return answer