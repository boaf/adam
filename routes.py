from flask import Flask, render_template

from eveapi import eve_parser, SkillTreeParser

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/skills')
def skills():
    skills = eve_parser(SkillTreeParser)
    return render_template('skills.html', skills=skills)

@app.route('/humans.txt')
def humans_txt():
    response = app.make_response(open('humans.txt').read())
    response.content_type = "text/plain"
    return response

if __name__ == '__main__':
    app.run(debug=True)