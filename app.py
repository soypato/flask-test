from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = [
    "basketball",
    "football",
    "voleyball"
]

database = {

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
  if not request.form.get("name"):
      return render_template("failure.html", message="Missing name :(")
  if not request.form.get("sport"):
      return render_template("failure.html", message="Missing sport :(")
  if request.form.get("sport") not in SPORTS:
      return render_template("failure.html", message="Invalid sport :(")
  return render_template("success.html")
