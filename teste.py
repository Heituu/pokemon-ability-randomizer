from flask import Flask
from flask import render_template
from flask import request
import requests
import random

app = Flask(__name__)


@app.route("/", methods =["GET", "POST"])
def homepage():
    if request.method == "POST":
        nhab = request.form.get("nhab")
        num = int(nhab)
        random_abilities = (random.sample(abilities, k=num))
        return render_template("index.html", resultado=random_abilities)
    else :
        return render_template("index.html")


url = "https://pokeapi.co/api/v2/ability"

response = requests.get(url, params={"limit" : 371})

dados = response.json()

hab = dados["results"]

abilities = []

for i in hab:
    abilities.append(i["name"])


if __name__ == "__main__":
    app.run()


