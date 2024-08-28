#Imports
import csv
import Webscraping as ws
#Functions
#Converting From the genre list STRING to an actual list
def listGenresConvert(genreString):
    genreString = genreString.replace("[", "")
    genreString = genreString.replace("]", "")
    genreString = genreString.replace("'", "")
    genreList = genreString.split(", ")
    return genreList

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
            if movieName.title() == row[0].title():
                #If found in database
                print("Movie found in database.")
                return True
        #If not found in database
        print("Movie not found in database.")
        return False

def writeMoiveStats(movieData = ["none"]):
    #Error Check
    if movieData == ["none"] or len(movieData) != 8:
        return ["Movie Data missing/ Invalid."]
    #Check if already in database by Title
    if not checkDatabase(movieName = movieData[0]):
        #Adding movieData to database
        with open("static/database.csv", "a", newline="") as database:
            writer = csv.writer(database, delimiter=",")
            writer.writerow(movieData)

def returnMovieStats(movieName="none"):
    #Error Check
    if movieName == "none":
        return "Title missing."
    #Checking if in Database
    if not checkDatabase(movieName.title()):
        #Accessing MovieDB API and writing data into database
        movieStats = ws.returnMovieDBData(movieName = movieName)
        writeMoiveStats(movieData = movieStats)
        movieStats[6] = listGenresConvert(movieStats[6])
        return movieStats
    #If in database
    with open("static/database.csv", newline="") as database:
        reader = csv.reader(database, delimiter=",")
        for row in reader:
            if row[0].title() == movieName.title():
                row[6] = listGenresConvert(row[6])
                return row