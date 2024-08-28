import requests
from bs4 import BeautifulSoup
import Database as db
#Class init
class movieStats:
    def __init__(self, Title, Summary, Rating, ReleaseDate, Length,  Director, GenreList, posterLink):
        self.title = Title
        self.summary = Summary
        self.rating = f"{round(Rating/2)}/10"
        self.releaseDate = ReleaseDate
        self.length = Length
        self.director = Director
        self.genreList = GenreList
        self.posterLink = posterLink

#The Moviedb
global genreDict
Moviedb_APIKEY = "66ab025a7673a17b6e9789838dc21fc0"
#Creating the Genre Dictionary
genreURL = f"https://api.themoviedb.org/3/genre/movie/list?api_key={Moviedb_APIKEY}"
response = requests.get(genreURL)
genreData = response.json()
genreDict = {genre["id"]: genre["name"] for genre in genreData["genres"]}

#Function(s) for Moviedb
def returnMovieDBData(Moviedb_APIKEY = "66ab025a7673a17b6e9789838dc21fc0", movieName = "none"):
    #Error Check
    if movieName == "none":
        return ["Movie name missing/invalid"]
    #Getting General Data
    dataURL = f"https://api.themoviedb.org/3/search/movie?api_key={Moviedb_APIKEY}&query={movieName}"    
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
    #holy large return statement
    movieData =  movieStats(movie["title"].title(),
                            movie["overview"],
                            movie["vote_average"],
                            movie["release_date"],
                            movie.get("runtime"),
                            directorList,
                            genreList,
                            f"https://image.tmdb.org/t/p/original/{movie["poster_path"]}")
    return movieData
#Odeon
#Showcase
#Vue
#Cineworld
#Savoy