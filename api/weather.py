import requests
import json

class Weather():

    def get_weather(self, lat, long):
        url = "http://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(long)+"&appid=35089fbc89289158d1d7f63b28f24a54&units=metric"

        res = requests.get(url)
        
        data = res.json()

        result={}
        res={}
        list1=[]
        result['temp'] = data["main"]["temp"]
        result['cloud'] = data["weather"][0]["main"]
        result['wind_speed'] = data["wind"]["speed"]
        result['humidity'] = data["main"]["humidity"]


        #temp : data = data["main"][0]["temp"]
        #cloud : data = data["weather"][0]["main"]
        #windspeed : data = data["wind"][0]["speed"]
        #humidity : data = data["main"][0]["humidity"]
        #temp,cloud,windspeed,humidity
        #result=json.dumps(result,4)
        return json.loads(json.dumps(result))