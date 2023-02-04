import urllib.request
import json

keyFile = open('keys', 'r')
api_key = keyFile.readline().rstrip()

api_endpoint = "https://api.openweathermap.org/data/2.5/weather"

# for Longitude and Latitude Input
#lat = input("Enter a Latitude: ")
#lon = input("Enter a Longitude: ")

# for City Name Input
city = input("Enter a city: ")
country_code = input("Enter a country code: ")
limit = "1"

#api_call = api_endpoint + "?lat=" + lat + "&lon=" + lon + "&appid=" + api_key
api_call = api_endpoint + "?q=" + city + ',' + country_code + "&limit=" + limit + "&appid=" + api_key
api_call = api_call.replace(" ", "%20")

with urllib.request.urlopen(api_call) as url:
	response = url.read()

parseResponse = json.loads(response.decode('utf-8'))

temperature = int(parseResponse['main']['temp']) - 273.15
feels_like = int(parseResponse['main']['feels_like']) - 273.15
weather = parseResponse['weather'][0]['description']

print('The weather in {} is {}, with a temperature of {:.0f}, but feels like {:.0f}.'.format(city, weather, temperature, feels_like))
