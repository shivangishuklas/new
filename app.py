from flask import Flask,render_template,redirect,request
import os
import sys


app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/musgen',methods=["GET", "POST"])
def musgen():
    if request.method == "POST":
        return render_template("index.html")
    else:
        return render_template("musgen.html")

@app.route('/musgenInf',methods=["GET", "POST"])
def musgenInf():
    if request.method == "POST":
        return render_template("musgenInf.html")
    else:
        return render_template("musgenInf.html")

@app.route('/musgenInt',methods=["GET", "POST"])
def musgenInt():
    if request.method == "POST":
        return render_template("musgenInt.html")
    else:
        return render_template("musgenInt.html")
    
@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)

