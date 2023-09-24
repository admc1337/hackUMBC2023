import tkinter as tk
from curses import has_colors
from datetime import datetime, time
import random
from unittest import result
import apiclasses
import webscrape

#vars to store urls for webscraping and api call
weather_url = "https://api.open-meteo.com/v1"

xmas_url = 'https://www.imdb.com/list/ls000096828/'
halloween_url = 'https://www.imdb.com/list/ls000091321/'
romance_url = 'https://www.imdb.com/list/ls064427905/'
romcom_url = 'https://www.imdb.com/list/ls053605210/'
comedy_url = 'https://www.imdb.com/list/ls058726648/'
animated_url = 'https://www.imdb.com/search/title/?title_type=feature&genres=animation'
action_url = 'https://www.imdb.com/search/title/?genres=action&groups=top_250&sort=user_rating,desc'
horror_url = 'https://www.imdb.com/list/ls003174642/'
scifi_url = 'https://www.imdb.com/search/title/?genres=sci_fi&num_votes=1000,&sort=user_rating,desc&title_type=feature'
thriller_url = 'https://www.imdb.com/search/title/?genres=thriller&groups=top_250&sort=user_rating,desc'

movieGenreList = [xmas_url, halloween_url, romance_url, romcom_url, comedy_url, animated_url, action_url, horror_url, scifi_url, thriller_url]
movieHolidayList = [xmas_url, halloween_url, romance_url]

#lists created to use later for algorithm
noRainDay = ['0','1','2']
noRainMovie = [romcom_url, romance_url, comedy_url, animated_url, action_url, scifi_url]
cloudToLightRain = ['3','45','48','51','53','55']
cloudToMovie = [romance_url, romcom_url, animated_url, action_url, scifi_url, thriller_url]
rainDay = ['56','57','61','63','65','66','67']
rainMovie = [romance_url, romcom_url, scifi_url, animated_url, thriller_url]
snowDay = ['71', '73','75','77']
snowMovies = [romance_url, romcom_url, animated_url]
stormDay = ['80','81','82','85','86','95','96','99']
stormMovie = [action_url, horror_url, scifi_url, thriller_url]

#creating classes for api call and web scraping call
weatherReport = apiclasses.weatherClient(weather_url)
movieTest = webscrape.webScraper
moviePicked = []
#to be used in api call
weatherEndpoint = 'forecast'
#uses zipcode entered to find correct lat and long coords to conduct weather call
def findZip(zipcode):
        with open('/Users/alejandro/Documents/VSCode Folder/hackUMBC2023/zipcode.txt','r') as file:
            lines = file.readlines()

            for line_number, line in enumerate(lines, start=1):
                if zipcode in line:
                    return lines[line_number - 1].strip()
            return print("Zipcode not found")
#to find current date
def findDate():
    currentTime = datetime.now()
    currentDate = currentTime.date().month
    return currentDate
#a function call so tkninter can use 
def runApp():
    zipcode = zip_entry.get()
    #formats zip entry correctly to be used in api call
    zipcode_in_list = findZip(zipcode).split(',')
    lat = zipcode_in_list[1].replace(' ','')
    long = zipcode_in_list[2].replace(' ','')
#params to get correct api data
    weatherParams = {
        'latitude': float(lat),
        'longitude': float(long),
        'hourly': 'is_day',
        'daily': 'temperature_2m_max,temperature_2m_min,sunrise,sunset',
        "current_weather": True,
        "temperature_unit": "fahrenheit",
        "windspeed_unit": "mph",
        "precipitation_unit": "inch",
        "timezone": "America/New_York",
        "forecast_days": 1,
    }
    #makes class and execs api call function
    weatherResults = weatherReport.make_request(weatherEndpoint, weatherParams)
    #to check if api did respond and give value
    if weatherResults is not None:
        current_weather = weatherResults.get('current_weather')
        daily_weather = weatherResults.get('daily')
        dateNow = findDate()
        weatherCode = current_weather['weathercode']
        
    #prints to console to check for correct data 
        print("Current Weather:")
        print(f"Temperature: {current_weather['temperature']}")
        print(f"Max Temperature: {daily_weather['temperature_2m_max']}")
        print(f"Min Temperature: {daily_weather['temperature_2m_min']}")
    #converts values to be used in tkinter app
        temp = str(current_weather['temperature'])
        max = str(daily_weather['temperature_2m_max'])
        min = str(daily_weather['temperature_2m_min'])

        weather_label.config(text='Current Weather:\nTemperature: '+temp+'\nHigh: '+max+'\nMin: '+min)


    #algorithm starts here, checks for holidays to recommend holiday specific movies
        if dateNow == 12:
            movieTest.scrapeMe(xmas_url)
        elif dateNow == 10:
            movieTest.scrapeMe(halloween_url)
        elif dateNow == 2:
            movieTest.scrapeMe(romance_url)
        else:
        #if not holiday, then checks weather data to recommend movie based on 'vibe'
        #the movie data is then used to populate the label
            if weatherCode in noRainDay:
                randUrl = random.choice(noRainMovie)
                moviePicked = movieTest.scrapeMe(randUrl)
                movie_label.config(text=f'Movie: '+ moviePicked['Title']+ '\n Year Released: ' + moviePicked['Year'])
            elif weatherCode in cloudToLightRain:
                randUrl = random.choice(cloudToMovie)
                moviePicked = movieTest.scrapeMe(randUrl)
                movie_label.config(text=f'Movie: '+ moviePicked['Title']+ '\n Year Released: ' + moviePicked['Year'])
            elif weatherCode in rainDay:
                randUrl = random.choice(rainMovie)
                moviePicked = movieTest.scrapeMe(randUrl)
                movie_label.config(text=f'Movie: '+ moviePicked['Title']+ '\n Year Released: ' + moviePicked['Year'])
            elif weatherCode in snowDay:
                randUrl = random.choice(snowMovies)
                moviePicked = movieTest.scrapeMe(randUrl)
                movie_label.config(text=f'Movie: '+ moviePicked['Title']+ '\n Year Released: ' + moviePicked['Year'])
            else:
                randUrl = random.choice(stormMovie)
                moviePicked = movieTest.scrapeMe(randUrl)
                movie_label.config(text=f'Movie: '+ moviePicked['Title']+ '\n Year Released: ' + moviePicked['Year'])
        

    else:
        #if fails to even get api response
        print("API error")
#creates a basic tkinter app to display and interact from user 
window = tk.Tk()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
wantWidth = int(screenWidth * .75)
wantHeight = int(screenHeight * .75)
window.geometry(f'{wantWidth}x{wantHeight}')
window.title('Weather Watchlist')

label = tk.Label(window, text='Enter Zipcode:')
zip_entry = tk.Entry(window)
get_button = tk.Button(window, text='Get your weather watchlist', command=runApp)
weather_label = tk.Label(window, text='')
movie_label = tk.Label(window, text='')

label.grid(row=0,column=0)
zip_entry.grid(row=1,column=0)
get_button.grid(row=2,column=0)
weather_label.grid(row=2, column=3)
movie_label.grid(row=2,column=1)

window.mainloop()

