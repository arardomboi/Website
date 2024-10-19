#IMPORTS
from flask import Flask, render_template, request #not me
import SQL #me
import Registration as reg #me
import Webscraping as wb #me

#FLASK

app = Flask(__name__, template_folder = "templates")

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
    movieClass = SQL.returnMovieDataByName(movieName)
    if movieClass:
        return "<h1>sigma rizz</h1>"

@app.route("/Log-in", methods = ["GET", "POST"])
def logPage():
    if request.method == "GET":
        return render_template("Log In.html")
    else: #method == POST
        return "<h1>Error :(</h1>"

@app.route("/Sign-up", methods = ["GET", "POST"])
def signPage():
    if request.method == "GET":  #Use form
        print("Rendering reg with type = 2.")
        return render_template("Registration.html", sendType = 2)
    else: #method == POST
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        uname = request.form.get("uname")
        gender = request.form.get("gender")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        checkPass = reg.checkPassword(password1) #dict of keys (lengthBool, numBool, specialBool)
        checkEmail = reg.checkEmail(email)
        if (checkPass["lengthBool"] and checkPass["numBool"] and checkPass["specialBool"]) and (checkEmail) and (password1 == password2): #holy
            userClassInstance = reg.userClass(firstName = fname, lastName = lname, userName = uname, gender = gender, email = email, password = password1)
            SQL.addUserDataToUserTable(userClassInstance)
            print(f"User Class instance with username '{userClassInstance.userName}' created.") 
            print("Rendering reg with type = 1.")
            return render_template("Registration.html", sendType = 1)
        else:
            print("Rendering reg with type = 3.")
            return render_template("Registration.html", sendType = 3, passwordError = checkPass)

if __name__ == "__main__":
    app.run(debug=True)
