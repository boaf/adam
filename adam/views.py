import os

from flask import render_template

from adam import app
from adam.cache import Cache
import eveapi

api = eveapi.EVEAPIConnection(cacheHandler=Cache(debug=True))

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/skills')
def skills():
    skilltree = api.eve.SkillTree()
    return render_template('skills.html', skilltree=skilltree)

@app.route('/humans.txt')
def humans_txt():
    response = app.make_response(open(os.path.dirname(os.path.realpath(__file__)) + '/../AUTHORS').read())
    response.content_type = "text/plain"
    return response
