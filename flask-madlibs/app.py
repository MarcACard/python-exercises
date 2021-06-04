from flask import Flask, render_template, request
from static.stories import *

app = Flask(__name__)


@app.route("/")
def home():
    """Generate a form based on a madlib story and prompt the user for answers"""
    return render_template("index.html", prompts=story.prompts)


@app.route("/story", methods=["POST"])
def generate_story():
    """Construct the user story from their submitted answers and render it to the user."""
    user_answers = request.form.to_dict()
    user_story = story.generate(user_answers)

    return render_template("story.html", story=user_story)
