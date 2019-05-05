# To generate Pipefile.lock used to specify run environment:    pipenv lock
# To get dependecies:                                           pipenv install --ignore-pipfile
# To run:                                                       pipenv run ./weather.py

# LED/GPIO Legend
#   Blue(27): Rain, Drizzle, Mist, Thunderstorm
#   Green(22): Sunny, Clear
#   Yellow(17): Snow, Clouds, Fog
#   Red(4): Unknown

import time
import datetime
import requests
from gpiozero import LED

# Constants
SAMPLE_API_KEY = "b6907d289e10d714a6e88b30761fae22"
API_KEY = "7592c66b736724c6f25034878fe84abb"
API_BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?APPID={API_KEY}"

BLUE_LED = 27
GREEN_LED = 22
YELLOW_LED = 17
RED_LED = 4

def main():
    while (True):
        message = ""
        condition = ""
        weather_data = get_current_weather_data()

        if (weather_data != None):
            weather_json = weather_data.json()
            if (weather_json['weather'] != None):
                condition = weather_json['weather'][0]['main']
                message = f"[{get_timestamp()}] Weather condition: {condition}"
            else:
                message = "Error: 'weather_json[\'weather\']' is null"
        else:
            message = "Error: 'weather_data' is null"

        print(message)
        update_led(condition)
        time.sleep(15)

def get_current_weather_data():
    response = requests.get(f'{API_BASE_URL}&zip=63129,us')
    return response

def get_timestamp():
    timestamp = time.time()
    formatted_timestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return formatted_timestamp

def update_led(condition):
    if (condition == 'Rain' or condition == 'Drizzle' or condition == 'Mist' or condition == 'Thunderstorm'):
        turn_off_LEDs()
        LED(BLUE_LED).on()
    elif (condition == 'Sunny' or condition == 'Clear'):
        turn_off_LEDs()
        LED(GREEN_LED).on()
    elif (condition == 'Snow' or condition == 'Clouds' or condition == 'Fog'):
        turn_off_LEDs()
        LED(YELLOW_LED).on()
    else:
        turn_off_LEDs()
        LED(RED_LED).on()

def turn_off_LEDs():
    LED(BLUE_LED).off()
    LED(GREEN_LED).off()
    LED(YELLOW_LED).off()
    LED(RED_LED).off()


main()