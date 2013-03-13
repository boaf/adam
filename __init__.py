from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'adam'}
app.config['SECRET_KEY'] = "A9D'y4WI@yf{d2/1=;pw=END[odzH62oC8iO+0b))1tD63HT2<tgJ{>e'2)?l@*"

db = MongoEngine(app)