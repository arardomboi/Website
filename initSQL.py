#Imports
import sqlite3 as sql #not me
import Webscraping as wb #me
import Registration as reg #me
#Yea
print("Connecting to database.")
global cursor
conn = sql.connect("static/Database.db", check_same_thread=False)
cursor = conn.cursor()
print("Connected successfully.")
#Moviedb Table
def createTableMovieData():
    cursor.execute("""CREATE TABLE movieData (
                   movieID INTEGER PRIMARY KEY AUTOINCREMENT,
                   movieName VARCHAR(50),
                   movieSummary TEXT,
                   movieRating VARCHAR(10),
                   movieReleaseDate CHAR(8),
                   movieLength VARCHAR(10),
                   movieDirector VARCHAR(50),
                   movieGenre TEXT,
                   moviePosterLink VARCHAR(200)
                   );""")
    print("Table 'movieData' made.")

def deleteTableMovieData():
    try:
        cursor.execute("DROP TABLE movieData;")
        print("Table 'movieData' deleted successfully.")
    except:
        print("Error deleting table 'movieData'.")

#Sign Up/ Log In
#functions


def createUserTable():
    cursor.execute("""CREATE TABLE userData (
                   userID INTEGER PRIMARY KEY AUTOINCREMENT,
                   firstName VARCHAR(50),
                   lastName VARCHAR(50),
                   userName VARCHAR (30),
                   email VARHCAR(100) NOT NULL,
                   hashedPassword TEXT NOT NULL,
                   gender CHARACTER);""")

def resetUserTable():
    try:
        cursor.execute("""DROP TABLE userData;""")
        createUserTable()
    except:
        createUserTable()
    print("UserData table reset successfully.")

def createReviewDataTable():
    cursor.execute("""CREATE TABLE reviewData (
                   reviewID INTEGER PRIMARY KEY AUTOINCREMENT,
                   movieID INTEGER,
                   userID INTEGER,
                   reviewText TEXT,
                   movieRating INTEGER,
                   reviewDate DATE,
                   FOREIGN KEY (movieID) REFERENCES movieData(movieID),
                   FOREIGN KEY (userID) REFERENCES userData(userID));""")

def resetReviewDataTable():
    try:
        #delete
        cursor.execute("DROP TABLE reviewData")
        #create
        createReviewDataTable()
    except:
        createReviewDataTable()
    print("ReviewData table reset.")