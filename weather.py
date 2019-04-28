import time
import requests

# Constants
API_KEY = "7592c66b736724c6f25034878fe84abb"
API_BASE_URL = f"api.openweathermap.org/data/2.5/weather?APPID={API_KEY}"

def main():
    weather_json = get_current_weather_data().json()
    print(weather_json['weather'][0]['main'])
    time.sleep(15)

def get_current_weather_data():
    #response = requests.get(f'{API_BASE_URL}&zip=63129,us')
    response = requests.get('https://samples.openweathermap.org/data/2.5/weather?zip=63129,us&appid=b6907d289e10d714a6e88b30761fae22')
    return response

main()