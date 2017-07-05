import urllib
"""
    Simple Weather API using the open weather data API
    In this app, you'll be entering the city of choice,
    and you'll be able to know the current weather there :D
"""
#city = raw_input('Enter your city\n')
response = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q=Kampala&APPID=4cdcbe29c9a481e33adf4d520f072685").read()
print response