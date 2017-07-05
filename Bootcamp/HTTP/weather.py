import urllib
import json
"""
    Simple Weather API using the open weather data API
    In this app, you'll be entering the city of choice,
    and you'll be able to know the current weather there :D
"""
city = raw_input('Enter your city\n')
url = 'http://api.openweathermap.org/data/2.5/weather'
values = {'APPID': '4cdcbe29c9a481e33adf4d520f072685', 'q': city}
data = urllib.urlencode(values)

response_string = urllib.urlopen('http://api.openweathermap.org/data/2.5/weather?%s' % data).read()
json = json.loads(response_string)
#print response_string
#print json
print 'The weather in {} is {}'.format(city, json['weather'][0]['description'])