from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = [
    "basketball",
    "football",
    "voleyball"
]

DATABASE = {

}

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name")
    return render_template("greet.html", name=name, sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():   
  name = request.form.get("name")
  sport = request.form.get("sport")
  
  if not name:
      return render_template("failure.html", message="Missing name :(")

  if not sport:
      return render_template("failure.html", message="Missing sport :(")

  if sport not in SPORTS:
      return render_template("failure.html", message="Invalid sport :(")
  

  DATABASE[name] = sport
  print(f"{DATABASE}")
  return render_template("success.html")
