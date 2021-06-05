from flask import Flask, render_template, request, session
from random import choice
from scripts.stories import *


app = Flask(__name__)
app.config["SECRET_KEY"] = "SHHHHHHHHHHH"

@app.route("/")
def home():
    """Generate a form based on a madlib story and prompt the user for answers"""
    # ? Does Python support destructuring similar to JS? It seems like it
    # ? would be useful here.
    random_story = STORIES[choice(list(STORIES.keys()))]

    session['story'] = str(random_story["id"])
    return render_template(
        "index.html",
        prompts=random_story["prompts"],
        title=random_story["story_name"]
    )


@app.route("/story", methods=["POST"])
def generate_story():
    """Construct the user story from their submitted answers and render it to the user."""
    user_answers = request.form.to_dict()

    story_template = STORIES.get(session['story'], "")
    story = Story(
        story_template["story_name"],
        story_template["prompts"],
        story_template["story"]
    )

    user_story = story.generate(user_answers)

    return render_template("story.html", story=user_story, title=story.title)
