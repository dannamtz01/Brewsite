from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html", user="Danna Martinez")

@app.route("/breweries/")
def breweries():
    # Fetching data from the openbrewerydb API
    response = requests.get("https://api.openbrewerydb.org/v1/breweries")
    data = response.json()
    return render_template("breweries.html", user="Danna Martinez", content=data)

@app.route("/beer_types/")
def beer_types():
    return render_template("beer_types.html", user="Danna Martinez")

@app.route("/about/")
def about():
    return render_template("about.html", user="Danna Martinez")

if __name__ == "__main__":
    app.run(debug=True)