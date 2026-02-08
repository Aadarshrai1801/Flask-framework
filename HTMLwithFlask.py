# Integrating HTML file with Flask framework

# Flask Framework

from flask import Flask, render_template

# It creates an instace of the Flask class, which will be your WSGI(Web Server Gateway Interface) application.

# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome() :
    return "<html><h1>Welcome to the world of Aadarsh...</h1></html>"

@app.route("/index")
def index() :
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__" :
    app.run(debug = True)