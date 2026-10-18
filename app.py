from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "KSNDJJSIN12HJS87A"



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/compare")
def compare():
    return render_template("compare.html")

@app.route("/specs")
def specs():
    return render_template("spect.html")

@app.route("/readme")
def readme():
    return render_template("readme.html")

if __name__ == "__main__":
    app.run(debug=True)
