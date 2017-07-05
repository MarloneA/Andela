import urllib
import json
"""
    Simple Weather app using the Open Weather Map API.
    In this app, you'll be entering the city of choice,
    and you'll be able to know the current weather in that city :D
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