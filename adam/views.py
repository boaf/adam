from adam import app
from flask import render_template
from eve_api import SkillTree

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/skills')
def skills():
    return render_template('skills.html', skills=SkillTree().get_skills())

@app.route('/humans.txt')
def humans_txt():
    response = app.make_response(open('static/humans.txt').read())
    response.content_type = "text/plain"
    return response