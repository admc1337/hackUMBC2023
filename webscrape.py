import requests
import random
from bs4 import BeautifulSoup

class webScraper:
    def __init__(self) -> None:
        pass
    #scrape command 
    def scrapeMe(url):
        response = requests.get(url)
        #if successful url response
        if response.status_code == 200:
            page = BeautifulSoup(response.text, 'html.parser')

            movieItems = page.find_all("div", class_="lister-item-content")
            movie = []
            for index, item in enumerate(movieItems, start = 1):
                title = item.find("h3", class_="lister-item-header").a.text.strip()
                year = item.find("span", class_="lister-item-year").text.strip("()")
                
                movie.append({
                    'Title': title,
                    'Year': year,
                })
            #prints to console to check for correct info and is returned to be used 
            moviePicked = random.choice(movie)
            print(moviePicked)
            return moviePicked

        else:
            print("Failed to get page: ", response.status_code)