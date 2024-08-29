#Imports
import csv
import Webscraping as ws
#Class
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

#Functions
#Converting From the genre list STRING to an actual list
"""
def listGenresConvert(genreString):
    genreString = genreString.replace("[", "")
    genreString = genreString.replace("]", "")
    genreString = genreString.replace("'", "")
    genreList = genreString.split(", ")
    return genreList
"""
def checkDatabase(movieName = "none"):
    #Error Check
    if movieName == "none":
        print("Movie name missing.")
        return False
    #Open File
    with open("static/database.csv", newline="") as database:
        reader = csv.reader(database, delimiter=",")
        #Loop through file
        for row in reader:
            if movieName.title == row[0]:
                #If found in database
                print("Movie found in database.")
                return True
        #If not found in database
        print("Movie not found in database.")
        return False

def writeMoiveStats(movieData = ["none"]):
    #Error Check
    if movieData == ["none"]:
        return ["Movie Data missing/ Invalid."]
    #Check if already in database by Title
    if not checkDatabase(movieName = movieData.title):
        #Adding movieData to database
        with open("static/database.csv", "a", newline="") as database:
            writer = csv.writer(database, delimiter=",")
            writer.writerow([movieData.title, movieData.summary, movieData.rating, movieData.releaseDate, movieData.length, movieData.director, movieData.genreList, movieData.posterLink])

def returnMovieStats(movieName="none"):
    #Error Check
    if movieName == "none":
        return "Title missing."
    #Checking if in Database
    if not checkDatabase(movieName.title()):
        #Accessing MovieDB API and writing data into database
        movieStats = ws.returnMovieDBData(movieName = movieName)
        writeMoiveStats(movieData = movieStats)
        return movieStats
    #If in database
    with open("static/database.csv", newline="") as database:
        reader = csv.reader(database, delimiter=",")
        for row in reader:
            if row[0].title() == movieName.title():
                movieData = movieStatsClass(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                return movieData