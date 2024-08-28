#IMPORTS
from flask import Flask, render_template
import Database as db
#PYTHON

def removeURLPunctuation(movieName):
    #Define Illegal Chars
    illegalChar = ["!","£","$","%","^",",",".","+","-",":",";"]
    specialChar = ["&"]
    encodedName = ""
    #Loop through for illegal Chars
    for letter in movieName:
        if letter == " ":
            encodedName += "-"
        elif not (letter in illegalChar):
            encodedName += letter
    encodedName = encodedName.replace("--", "-") #Removes double dashes (double spaces)
    return encodedName

#FLASK

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/movie")
def movieBase():
    movieDataTemplate = ["Title", "Summmary", "Rating", "Release Date", "Movie Length", "Directors", ["Genre 1","Genre 2","Genre 3", "Genre 4"], "Image link"]
    return render_template("movie.html", movieData = movieDataTemplate)
@app.route("/movie/<movieName>")
def moviePage(movieName):
    movieData = db.returnMovieStats(movieName)
    return render_template("movie.html", movieData = movieData)

if __name__ == "__main__":
    app.run(debug=True)

print("Process Ended.")
