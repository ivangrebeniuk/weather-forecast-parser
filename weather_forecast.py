#! Python 3.7
# Script to parse data from weather forecast web site

import requests
from bs4 import BeautifulSoup


# Download web page
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071#.X0IsJS2w3q0')

# Create a BeautifulSoup class to parse the page
soup = BeautifulSoup(page.content, 'html.parser')

# Find the div with id seven-day-forecast, and assign to seven_day
seven_day = soup.find(id='seven-day-forecast')

# Inside seven_day, find each individual forecast item.
forecast_items = seven_day.find_all(class_='forecast-tombstone')
tonight = forecast_items[0]

# TODO Extract and print it
# print(tonight.prettify())
city = seven_day.find(class_='panel-title').get_text()
period = tonight.find(class_='period-name').get_text()
short_desc = tonight.find(class_='short-desc').get_text()
temp = tonight.find(class_='temp').get_text()
img = tonight.find('img')
desc = img['title']

periods = [i.get_text() for i in seven_day.select('.tombstone-container .period-name')]
short_descs = [i.get_text() for i in seven_day.select('.tombstone-container .short-desc')]
temps = [i.get_text() for i in seven_day.select('.tombstone-container .temp')]
descs = [i['title'] for i in seven_day.select('.tombstone-container img')]
# print(periods)
# print(short_descs)
# print(temps)
# print(descs)
with open('./forecast.txt', 'w') as f:
    f.write(f'Weather forecast in {city.strip()}:\n')
    ls = list(zip(periods, short_descs, temps, descs))
    for i in ls:
        s = " | ".join(i)
        f.write(s + '\n')
