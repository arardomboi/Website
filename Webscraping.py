import requests
import bs4 as bs
import urllib.request
#Class init
class movieStatsClass:
    def __init__(self, Title, Summary, Rating, ReleaseDate, Length,  Director, GenreList, posterLink):
        self.title = Title
        self.summary = Summary
        self.rating = f"{round(Rating/2)}/10"
        self.releaseDate = ReleaseDate
        self.length = Length
        self.director = Director
        self.genreList = GenreList
        self.posterLink = posterLink
    def returnAsList(self):
        return [self.title, self.summary, self.rating, self.releaseDate, self.length, self.director, self.genreList, self.posterLink]

#The Moviedb
global genreDict
Moviedb_APIKEY = "66ab025a7673a17b6e9789838dc21fc0"
#Creating the Genre Dictionary
genreURL = f"https://api.themoviedb.org/3/genre/movie/list?api_key={Moviedb_APIKEY}"
response = requests.get(genreURL)
genreData = response.json()
genreDict = {genre["id"]: genre["name"] for genre in genreData["genres"]}

#Function(s) for Moviedb
def returnMovieDBData(movieName = "none", Moviedb_APIKEY = "66ab025a7673a17b6e9789838dc21fc0"):
    #Error Check
    if movieName == "none":
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
    #checking if runtime returns 'None'
    if not movie.get("runtime"):
        print(f"Error returning '{movieName.title()}'runtime, defaulting to 138.")
        movieRuntime = 138
    else:
        movieRuntime = movie.get("runtime")
    #holy large return statement
    return [movie["title"].title(),
            movie["overview"],
            movie["vote_average"],
            movie["release_date"],
            movieRuntime, #keeps returning "None"
            directorList[0],
            genreList,
            f"https://image.tmdb.org/t/p/original/{movie["poster_path"]}"]
#Odeon - bs4 not work
    #bs4 doesn't work
pass
#Showcase
    #bs4 works
showcaseSourceURL = urllib.request.urlopen("").read()
soup = bs.BeautifulSoup(showcaseSourceURL, "lxml")

pass
#Vue

pass
#Cineworld
pass
#Savoy
pass