import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from eveapi import eve_parser, SkillTreeParser

from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/skills')
def skills():
    skills = eve_parser(SkillTreeParser)
    return render_template('skills.html', skills=skills)

@app.route('/humans.txt')
def humans_txt():
    response = app.make_response(open('static/humans.txt').read())
    response.content_type = "text/plain"
    return response

if __name__ == '__main__':
    app.run(debug=True)