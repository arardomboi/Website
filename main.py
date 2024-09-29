#IMPORTS
from flask import Flask, render_template #not me
import sql #me
#PYTHON



#FLASK

app = Flask(__name__)

@app.route("/")
def home():
    print("Rendering home page.")
    return render_template("home.html")

@app.route("/search")
def search():
    print("Rendering Search page")
    return render_template("search.html")

@app.route("/movie")
def movieBase():
    print("Rendering base movie template.")
    movieDataTemplate = ["Title", "Summmary", "Rating", "Release Date", "Movie Length", "Directors", ["Genre 1","Genre 2","Genre 3", "Genre 4"], "Image link"]
    return render_template("movie.html", movieData = movieDataTemplate)

@app.route("/movie/<movieID>")
def moviePage(movieID):
    print(f"Rendering movie page with movieID as {movieID}.")
    movieDict = sql.returnMovieDataByID(movieID)

    return render_template("movie.html", movieDict = movieDict)

@app.route("/Log-in")
def logPage():
    return render_template("Registration.html", sendType = 1)

@app.route("/Sign-up")
def signPage():
    return render_template("Registration.html", sendType = 2)

if __name__ == "__main__":
    app.run(debug=True)