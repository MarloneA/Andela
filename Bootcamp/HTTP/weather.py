import urllib
import json
import re
"""
    Simple Weather app using the Open Weather Map API.
    In this app, you'll be entering the city of choice,
    and you'll be able to know the current weather in that city :D
"""
def get_city():
    city = raw_input('Enter your city\n')
    if re.match(r'^[a-zA-Z\s]+$', city):
        return city
    else:
        return get_city()

city = get_city()
url = 'http://api.openweathermap.org/data/2.5/weather'
values = {'APPID': '4cdcbe29c9a481e33adf4d520f072685', 'q': city}
data = urllib.urlencode(values)

response_string = urllib.urlopen('http://api.openweathermap.org/data/2.5/weather?%s' % data).read()
json = json.loads(response_string)

print 'The weather in {} is {}'.format(city, json['weather'][0]['description'])