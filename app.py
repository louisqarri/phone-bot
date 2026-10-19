from flask import Flask, render_template, redirect, url_for, request
from sqlalchemy import select
from brain import Brain

brain = Brain()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/compare", methods=["GET", "POST"])
def compare():
    result = None
    if request.method == "POST":
         model_one = request.form["model_one"]
         model_two = request.form["model_two"]
         result = brain.compare_phones(model_one.lower(), model_two.lower())
    return render_template("compare.html", phones=brain.all_phones, result=result)

@app.route("/specs", methods=["GET", "POST"])
def specs():
        result = None
        if request.method == "POST":
             model = request.form["model"]
             result = brain.show_phone_specs(model.lower())
        return render_template("specs.html", phones=brain.all_phones, result=result)

@app.route("/readme")
def readme():
    return render_template("readme.html")

if __name__ == "__main__":
    app.run(debug=True)
