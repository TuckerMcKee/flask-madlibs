
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "SecretKey"
debug = DebugToolbarExtension(app)

@app.route('/')
def form():
    return render_template("form.html",story=story)

@app.route('/story')
def story_render():
    answers = {}
    for word in story.prompts:
        answers[word] = request.args[word]
    return render_template('story.html',your_story=story.generate(answers))   




