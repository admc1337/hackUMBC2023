from fileinput import close
import requests

api_url = 'https://api.open-meteo.com/v1/forecast'

zipcode = input('What is the zipcode you want to check?: ')

def findZip(zipcode):
    with open('zipcode.txt','r') as file:
        lines = file.readlines()

        for line_number, line in enumerate(lines, start=1):
            if zipcode in line:
                return lines[line_number - 1].strip()
        return print("Zipcode not found")

zipcode_in_list = findZip(zipcode).split(',')
lan = zipcode_in_list[1].replace(' ','')
long = zipcode_in_list[2].replace(' ','')

params = {
    'latitude': float(lan),
    'longitude': float(long),
    "current_weather": True
}

response = requests.get(api_url, params=params)

if response.status_code == 200:
    data = response.json()

    current_weather = data.get("current_weather")
    if current_weather:
        print("Current Weather:")
        print(f"Temperature: {current_weather['temperature']} C")
        print(f"Conditions: {current_weather['weathercode']}")