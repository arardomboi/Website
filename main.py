#IMPORTS
from flask import Flask, render_template, request #not me
import sql #me
import Registration as reg
#PYTHON
pass
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

@app.route("/movie/<movieID>")
def moviePage(movieID):
    print(f"Rendering movie page with movieID as {movieID}.")
    movieDict = sql.returnMovieDataByID(movieID)
    return render_template("movie.html", movieDict = movieDict)

@app.route("/Log-in", methods = ["GET", "POST"])
def logPage():
    if request.method == "GET":
        return render_template("Registration.html", sendType = 1)
    else: #method == POST
        pass
    return "<h1>Error :(</h1>"

@app.route("/Sign-up", methods = ["GET", "POST"])
def signPage():
    if request.method == "GET": 
        return render_template("Registration.html", sendType = 2)
    else: #method == POST
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        uname = request.form.get("uname")
        gender = request.form.get("gender")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        if password1 != password2:
            return render_template("Registration.html", sendType = 3)
        if reg.checkPassword(password1):
            userClassInstance = reg.userClass(firstName = fname, lastName = lname, userName = uname, gender = gender, email = email, password = password1)
        else:
            return render_template("Registration.html", sendType = 3)
        pass
    return "<h1>Error :(</h1>"

if __name__ == "__main__":
    app.run(debug=True)