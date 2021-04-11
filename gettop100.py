import requests
from bs4 import BeautifulSoup


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

all_aiports = get_all_airports(url_list)

