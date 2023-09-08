import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime


def get_temperature():
    url = 'https://meteofor.com.ua/ru/weather-kremenchuk-4968/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        temperature_element = soup.find('div', class_='today-temp')

        if temperature_element:
            temperature = temperature_element.text.strip()
            return temperature
        else:
            return None
    else:
        return None



def save_to_database(temperature):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()


    cursor.execute('''CREATE TABLE IF NOT EXISTS weather_data
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       timestamp DATETIME,
                       temperature TEXT)''')

    timestamp = datetime.now()
    cursor.execute('INSERT INTO weather_data (timestamp, temperature) VALUES (?, ?)',
                   (timestamp, temperature))

    conn.commit()
    conn.close()



temperature = get_temperature()

if temperature:

    save_to_database(temperature)
    print(f'SAved to base: {temperature}')
else:
    print('Error to find temperature')