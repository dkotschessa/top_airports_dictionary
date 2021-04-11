import requests
from bs4 import BeautifulSoup
import json


url_list = {
    'North America' : 'https://www.flightsfrom.com/top-100-airports-in-north-america',
    'South America' : 'https://www.flightsfrom.com/top-100-airports-in-south-america',
    'Asia' : 'https://www.flightsfrom.com/top-100-airports-in-asia',
    'Europe' : 'https://www.flightsfrom.com/top-100-airports-in-europe'
}


def parse_top_airports(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    airports = []
    for span_tag in soup.find_all('span'):
        if '(' in span_tag.text:
            text = span_tag.text
            text = text.split('(')[1]
            text = text.split(')')[0]
            airports.append(text)
    return airports

def get_all_airports(url_list):
    airports = []
    for airport_url in list(url_list.values()):
        airport_list = parse_top_airports(airport_url)
        airports.extend(airport_list)
    return airports

all_airports = get_all_airports(url_list)

# need in format 
airports = [
  {
    "Airport" : "Philadelphia International Airport",
    "iata" : "PHL",
    "City" : "Philadelphia",
    "State": "PA"
  },
  {
    "Airport" : "Naples Municipal Airport",
    "iata" : "APF",
    "City" : "Naples",
    "State" : "Florida"
  }

]

# Current format of airports.json 
# (downloaded from https://gist.github.com/tdreyno/4278655/raw/7b0762c09b519f40397e4c3e100b097d861f5588/airports.json)
  [{
    "code": "ZVK",
    "lat": "16.5536",
    "lon": "104.763",
    "name": "Savannakhet Airport",
    "city": "Savannakhet",
    "state": "Savannahkhet",
    "country": "Laos",
    "woeid": "12514556",
    "tz": "Asia\/Vientiane",
    "phone": "",
    "type": "Airports",
    "email": "",
    "url": "",
    "runway_length": "5350",
    "elev": "509",
    "icao": "VLSK",
    "direct_flights": "3",
    "carriers": "1"
  }


def load_airports_dict():
    f = open('airports.json', 'r')
    airports_dict = json.load(f)
    return airports_dict

airport_dict = load_airports_dict()

def make_dict():
    my_airport_dict = []
    for airport in airport_dict:
        if airport['code'] in all_airports:
            print(airport['name'])
            entry = {
                'Airport' : airport['name'],
                'iata' : airport['code'],
                'icao' : airport['icao'],
                'City': airport['city'],
                'State' : airport['state'],
                'Country' : airport['country']
            }
            my_airport_dict.append(entry)
    return my_airport_dict


