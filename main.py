#IMPORTS
from flask import Flask, render_template, request, redirect, url_for #not me
import random as ran #not me
import requests as rq
import SQL #me
import Registration as reg #me
import Webscraping as wb #me
#PYTHON


#FLASK

app = Flask(__name__, template_folder = "templates")
@app.route("/rizz")
def temp():
    pageData = request.form
    print(pageData)
    return render_template("temp.html")

@app.route("/")
def home():
    print("Rendering home page.")
    return render_template("home.html")

@app.route("/search")
def search():
    print("Rendering Search page")
    return render_template("search.html")

@app.route("/movie/id/<movieID>") #if movie in db
def moviePage(movieID):
    print(f"Rendering movie page with movieID as {movieID}.")
    movieClass = SQL.returnMovieDataByID(movieID)
    return render_template("movie.html", movieClass = movieClass)

@app.route("/movie/name/<movieName>") #if movie not in db
def movieNameCall(movieName):
    print(f"Rendering movie with name {movieName}")
    movieClass = SQL.returnMovieDataByName(movieName) #collect data as a class
    return redirect(url_for("moviePage")) #redirecting to actual page

@app.route("/Log-in", methods = ["GET", "POST"])
def logPage():
    if request.method == "GET":
        return render_template("Log In.html")
    else: #method == POST
        return "<h1>Error :(</h1>" #NOT MADE YET

@app.route("/Sign-up", methods = ["GET", "POST"])
def signPage():
    if request.method == "GET":  #Use form
        print("Rendering Signup initial")
        return render_template("Sign Up.html", type = 1)
    else: #method == POST
        formData = request.form
        returnedFormData = reg.returnLogInFormData(formData)
        if returnedFormData[0]:
            userClassInstance = returnedFormData[1]
            SQL.addUserDataToUserTable(userClassInstance)
            return render_template("temp.html")
        else:
            pass

if __name__ == "__main__":
    app.run(debug=True)
