#imports
import urllib.request, json #not me
from flask import request
#functions
def returnSignFormData(page = None):
    with urllib.request.urlopen("/Sign-up") as url:
        data = json.load(url)
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        uname = request.form.get("uname")
        gender = request.form.get("gender")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        print(":)")