from cs50 import SQL
from flask import Flask, redirect, render_template, request

SPORTS = [
    "basketball",
    "football",
    "voleyball" 
]

app = Flask(__name__)

db = SQL("sqlite:///froshims.db")

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name")
    return render_template("greet.html", name=name, sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():   

    # Validate submission
    name = request.form.get("name") # Get form from HTML
    sport = request.form.get("sport") # Get form from HTML
    if not name or sport not in SPORTS: # Comprobation
        return render_template("failure.html")

    # Remember registrant
    db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)

    # Confirm registration
    return redirect("/success")

@app.route('/registrants')
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)

@app.route('/success')
def success():
    return render_template("success.html")

@app.route("/users_log")
def users_log():
    return render_template("users_log.html", )