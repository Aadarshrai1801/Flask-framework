# Building Url dynamically, Variable rule, and Jinja 2 Template engine

from flask import Flask, render_template,request

# Jinja 2 template engine
'''
{{}} --> Expressions to print output in html
{%...%} --> Conditions, for loops
{#...#} --> This is for the comments
'''

# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome() :
    return "<html><h1>Welcome to the world of Aadarsh...</h1></html>"

@app.route("/index",methods=["GET"])
def index() :
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method == "POST":
        name=request.form["name"]
        return f"Hello {name}"
    return render_template("form.html")

# Variable rule
@app.route("/success/<int:score>")
def success(score):
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template("result.html",results=res)

@app.route("/successres/<int:score>")
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
        
    exp={
        "score":score,
        "res":res
    }
    return render_template("result1.html",results=exp)

@app.route("/successif/<int:score>")
def successif(score):
    return render_template("result.html",results=score)
   
# Building URL dynamically


if __name__ == "__main__" :
    app.run(debug = True)