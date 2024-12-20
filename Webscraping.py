#imports
import requests #not me
from bs4 import BeautifulSoup #not me
import urllib.request #not me
import time #not me
import SQL #me
from flask import jsonify
#selenium - not me
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#Class init
class movieStatsClass:
    def __init__(self, Title, Summary, Rating, ReleaseDate, Length,  Director, GenreList, posterLink, ID = None):
        self.ID = ID
        self.title = Title
        self.summary = Summary
        self.rating = round(float(Rating))
        self.releaseDate = ReleaseDate
        self.length = Length
        self.director = Director
        self.genreString = GenreList
        self.posterLink = posterLink
    
    def returnAsList(self): #bit useless
        return [self.ID, self.title, self.summary, self.rating, self.releaseDate, self.length, self.director, self.genreList, self.posterLink]
    
    def returnGenreAsString(self): #useless
        genreString = self.genreList[0]
        for genre in self.genreList[1:]:
            genreString += (f", {genre}")
        return genreString
    
    def returnGenresAsList(self):
        genreList = self.genreString.split(",")
        return genreList

def classifyFromAPI(movieList):
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
        raise Exception(f"Movie name of {movieName} missing.")
    #Getting General Data
    dataURL = f"https://api.themoviedb.org/3/search/movie?api_key={Moviedb_APIKEY}&query={movieName}&append_to_response=runtime"
    response = requests.get(dataURL)
    data = response.json()
    #page of movie names
    moviePage = data["results"]
    #check first page
    temp = False
    for item in moviePage:
        if item["title"].lower() == movieName.lower():
            movie = item
            temp = True
    #if no names match
    if not temp:
        print(f"No data found for movie name {movieName}, defaulting to first item.")
        movie = moviePage[0]
    else:
        print(f"Exact movie with name '{movieName.title()}' found.")
    print(movie)
    #Get Director
    creditURL = f"https://api.themoviedb.org/3/movie/{movie["id"]}/credits?api_key={Moviedb_APIKEY}"
    creditResponse = requests.get(creditURL)
    creditData = creditResponse.json()
    director = "Unknown"
    for worker in creditData["crew"]:
        if worker["job"] == "Director":
            director = worker["name"]
            break
    #Getting Genres
    genreList = returnGenreList(movieName)
    genreString = SQL.convertListToString(genreList)
    #checking if runtime returns 'None' as it keeps returning none
    if not movie.get("runtime"):
        print(f"Error returning '{movieName.title()}' runtime")
        movieRuntime = -1
    else:
        movieRuntime = movie.get("runtime")
    #holy large shaboingery
    movieList =  [movie["title"].title(),
            movie["overview"],
            movie["vote_average"],
            movie["release_date"],
            movieRuntime,
            director,
            genreString,
            f"https://image.tmdb.org/t/p/original/{movie["poster_path"]}"]
    movieClass = classifyFromAPI(movieList)
    return movieClass

def returnGenreList(movieName = None, Moviedb_APIKEY = "66ab025a7673a17b6e9789838dc21fc0"): #remade for bug fixing
    movieURL = f"https://api.themoviedb.org/3/search/movie?api_key={Moviedb_APIKEY}&query={movieName}&append_to_response=runtime"
    response = requests.get(movieURL)
    data = response.json()
    pageData = data["results"][0]
    genreIDList = pageData["genre_ids"]
    genreList = []
    for genreID in genreIDList:
        genreList.append(genreDict[genreID])
    return genreList

def returnMovieDBLikeMovies(movieName = None, Moviedb_APIKEY = "66ab025a7673a17b6e9789838dc21fc0"):
    dataURL = f"https://api.themoviedb.org/3/search/movie?api_key={Moviedb_APIKEY}&query={movieName}&append_to_response=runtime"
    response = requests.get(dataURL)
    data = response.json()
    #page of movie names
    moviePage = data["results"]
    return moviePage

#Odeon
def returnODEONData(movieName = None):
    #error check
    if not movieName:
        return None
    # open page
    driverOptions = Options()
    driver = webdriver.Chrome()
    try: #try open on ODEON page
        driver.get("https://www.odeon.co.uk/")
        time.sleep(2)
        try: #accept cookies
            cookiesButton = driver.find_element(By.ID, "onetrust-accept-btn-handler")
            cookiesButton.click()
            time.sleep(1)
        except:
            pass
        #search BUTTON
        searchButton = driver.find_element(By.CLASS_NAME, "banner-icon")
        searchButton.click()
        time.sleep(1)
        #search BOX
        searchBox = driver.find_element(By.CLASS_NAME, "header-search-input")
        searchBox.send_keys(movieName)
        searchBox.send_keys(Keys.RETURN)
        time.sleep(3)
        
        #click on result
        movieLink = driver.find_element(By.XPATH, "//a[contains(@class, 'film-title')]")
        movieLink.click()
        time.sleep(3)  # Wait for the movie page to load
        
        # Scrape movie details
        title = driver.find_element(By.CLASS_NAME, "film-title").text
        releaseDate = driver.find_element(By.CLASS_NAME, "release-date").text
        runtime = driver.find_element(By.CLASS_NAME, "runtime").text
        genre = driver.find_element(By.CLASS_NAME, "genres").text
        #temp to check if data retrieval is possible
        movieData = {
            "Title": title,
            "Release Date": releaseDate,
            "Runtime": runtime,
            "Genre": genre,
        }
        print(movieData)
        return movieData
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

#returnODEONData("Wicked")
#Showcase
"""
movieName = "Venom"
showcaseURL = "https://www.showcasecinemas.co.uk"
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)
driver.get(showcaseURL)
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)
time.sleep(5)
try:
    print("Pressing un cookies")
    wait.until(EC.visibility_of_element_located((By.ID, "didomi-notice-agree-button"))).click()
except:
    pass
time.sleep(2)
print("Pressing on search BUTTON")
searchButton = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/div[1]/div[2]/header/div/div/div/div[2]/div/div[2]/div[2]/div/svg"))).click()
time.sleep(2)
print("Pressing on search INPUT BOX")
searchBox = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/div[1]/div[2]/header/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div/input"))).click()
time.sleep(2)
action.move_to_element(searchBox).click().send_keys(movieName).perform()
"""
###
"""
showcaseSoup = BeautifulSoup(showcaseURL, "html.parser")

"""
#Vue

#Cineworld
#Savoy