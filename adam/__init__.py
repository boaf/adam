import os
basedir = os.path.abspath(os.path.dirname(__file__))

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "A9D'y4WI@yf{d2/1=;pw=END[odzH62oC8iO+0b))1tD63HT2<tgJ{>e'2)?l@*"

from adam.db import db_session

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

from adam import views
