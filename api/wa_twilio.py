import os
from twilio.rest import Client

class Whatsapp():
    def send(self, sender, receiver, token):
        account_sid = 'AC8659350d2744b2f97ff52d29b2130491' 
        auth_token = '032e46b21d3f0be56bf436ab6bdd35c6' 
        client = Client(account_sid, auth_token) 
        
        message = client.messages.create( 
                                    from_='whatsapp:'+str(sender),  
                                    body='This is your token [ '+token+' ]',      
                                    to='whatsapp:'+str(receiver) 
                                ) 
        res = "Failed"
        if message.error_message==None:
            res = "Success"
        else:
            res = "Failed"
        return(res)