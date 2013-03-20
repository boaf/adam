import os
basedir = os.path.abspath(os.path.dirname(__file__))

from flask import Flask, g, session

from flask.ext.sqlalchemy import SQLAlchemy
from flask_openid import OpenID

app = Flask(__name__)
app.config['SECRET_KEY'] = "A9D'y4WI@yf{d2/1=;pw=END[odzH62oC8iO+0b))1tD63HT2<tgJ{>e'2)?l@*"

oid = OpenID(app)

from adam.db import db_session
from adam.models import User


@app.before_request
def before_request():
    g.user = None
    if 'openid' in session:
        g.user = User.query.filter_by(openid=session['openid']).first()

@app.after_request
def after_request(response):
    db_session.remove()
    return response

from adam import views
