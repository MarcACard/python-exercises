from flask import Flask, render_template, request
from random import choice
from scripts.stories import *


app = Flask(__name__)


@app.route("/")
def home():
    """Generate a form based on a madlib story and prompt the user for answers"""
    # ? Does Python support destructuring similar to JS? It seems like it
    # ? would be useful here.
    random_story = STORIES[choice(list(STORIES.keys()))]

    return render_template(
        "index.html",
        prompts=random_story["prompts"],
        title=random_story["story_name"],
        id=random_story["id"],
    )


@app.route("/story", methods=["POST"])
def generate_story():
    """Construct the user story from their submitted answers and render it to the user."""
    user_answers = request.form.to_dict()

    story_template = STORIES[user_answers.get("id", "")]
    story = Story(
        story_template["prompts"],
        story_template["story"],
        story_template["story_name"],
        story_template["id"],
    )

    user_story = story.generate(user_answers)

    return render_template("story.html", story=user_story, title=story.title)
