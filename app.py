import http.client
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Bienvenue sur Football Stats"

@app.route('/teams')
def teams():
    # conn = http.client.HTTPSConnection("v3.football.api-sports.io")
    #
    # headers = {
    #     'x-rapidapi-host': "v3.football.api-sports.io",
    #     'x-rapidapi-key': "7b5bd0444b772ea5848eebc8a730f77a"
    # }
    #
    #
    #
    # conn.request("GET", "/teams/statistics", headers=headers)
    #
    # res = conn.getresponse()
    # data = res.read()



    return render_template("teams.html")