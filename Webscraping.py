#imports
import requests
from bs4 import BeautifulSoup
import urllib.request
import time
#selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#Class init
class movieStatsClass:
    def __init__(self, Title, Summary, Rating, ReleaseDate, Length,  Director, GenreList, posterLink):
        self.title = Title
        self.summary = Summary
        self.rating = f"{round(float(Rating)/2)}/10"
        self.releaseDate = ReleaseDate
        self.length = Length
        self.director = Director
        self.genreList = GenreList
        self.posterLink = posterLink
    def returnAsList(self):
        return [self.title, self.summary, self.rating, self.releaseDate, self.length, self.director, self.genreList, self.posterLink] 

def classify(movieList):
    movieClass = movieStatsClass(movieList[0], movieList[1], movieList[2], movieList[3], movieList[4], movieList[5], movieList[6], movieList[7])
    return movieClass
#The Moviedb
global genreDict
Moviedb_APIKEY = "66ab025a7673a17b6e9789838dc21fc0"
#Creating the Genre Dictionary
genreURL = f"https://api.themoviedb.org/3/genre/movie/list?api_key={Moviedb_APIKEY}"
response = requests.get(genreURL)
genreData = response.json()
genreDict = {genre["id"]: genre["name"] for genre in genreData["genres"]}

#Function(s) for Moviedb
def returnMovieDBData(movieName = None, Moviedb_APIKEY = "66ab025a7673a17b6e9789838dc21fc0"):
    #Error Check
    if movieName == None:
        return ["Movie name missing/invalid"]
    #Getting General Data
    dataURL = f"https://api.themoviedb.org/3/search/movie?api_key={Moviedb_APIKEY}&query={movieName}&append_to_response=runtime"
    response = requests.get(dataURL)
    data = response.json()
    #NEED TO WORK ON
    movie = data["results"][0]
    #List of Directors
    creditURL = f"https://api.themoviedb.org/3/movie/{response.json()["results"][0]["id"]}/credits?api_key={Moviedb_APIKEY}"
    creditResponse = requests.get(creditURL)
    creditData = creditResponse.json()
    directorList = []
    for worker in creditData["crew"]:
        if worker["job"] == "Director":
            directorList.append(worker["name"])
    #Getting Genres
    genreURL = f"https://api.themoviedb.org/3/genre/movie/list?api_key={Moviedb_APIKEY}&lanuage=en-US"
    genreResponse = requests.get(genreURL)
    genreIDList = genreResponse.json().get("genres", [])
    genreList = []
    for genre in genreIDList:
        genreList.append(genre["name"])
    #checking if runtime returns 'None' as it keeps returning none
    if not movie.get("runtime"):
        print(f"Error returning '{movieName.title()}' runtime, defaulting to 138.")
        movieRuntime = 138
    else:
        movieRuntime = movie.get("runtime")
    #holy large return statement
    movieList =  [movie["title"].title(),
            movie["overview"],
            movie["vote_average"],
            movie["release_date"],
            movieRuntime,
            directorList[0],
            genreList,
            f"https://image.tmdb.org/t/p/original/{movie["poster_path"]}"]
    movieClass = classify(movieList)
    return movieClass

#Odeon
def returnODEONDates(movieName = None):
    delay = 0.5
    firefoxOptions = Options()
    #firefoxOptions.add_argument("--headless") #Cant see physical page on pc
    driver = webdriver.Firefox()
    browser = driver.get("https://www.odeon.co.uk")
    try:
        elem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))) #holy weird line
    except TimeoutError:
        driver.quit()
        returnODEONDates(movieName)
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click() #click on accept popup
    driver.find_element(By.CLASS_NAME, "banner-icon").click() #click on search box
    driver.quit()

"""
print("ODEON")
print("init firefox driver")
firefoxOptions = Options()
firefoxOptions.add_argument("--headless")
driver = webdriver.Firefox()

print("open website page")

driver.get("https://www.odeon.co.uk")

print("Sleep")
#sleep for website to load
t.sleep(5)

print("Sleep Done.\n Press Accept")
#press the accept button for ODEN website
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

print("Look for search bar.")
t.sleep(1)
#click on search button
driver.find_element(By.CLASS_NAME, "banner-icon").click()
print("typing in search bar.")
t.sleep(0.5)
#find search page
searchBar = driver.find_element(By.CLASS_NAME, "auto-complete")
driver.quit()
"""
#Showcase
    #bs4 works
"""showcaseSourceURL = urllib.request.urlopen("https://www.showcasecinemas.co.uk/movies/251633-deadpool-and-wolverine/").read()
soup = BeautifulSoup(showcaseSourceURL, "lxml")"""
#Vue
#Cineworld
#Savoy