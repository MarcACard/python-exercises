from flask import Flask, render_template, request, redirect, flash
from flask.templating import render_template_string
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "FaKe_SeCrEt_KeY"
toolbar = DebugToolbarExtension(app)


# Storing as List, sessions not yet learned.
responses = []


@app.route("/")
def home():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions

    return render_template(
        "index.html", title=title, instructions=instructions, is_index=True
    )


@app.route("/question/<q_num>")
def survey_question(q_num):
    """Render Survey Questions to user. Current functionality will prevent users from retaking the survery or accessing previous questions."""
    if len(satisfaction_survey.questions) == len(responses):
        flash("Survey Already Completed", "error")
        return redirect("/thank-you")

    if int(q_num) != len(responses):
        flash(
            "Attempted to access invalid question, or question already answered",
            "error",
        )
        return redirect(f"/question/{len(responses)}")

    # Render survey question info
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    question = satisfaction_survey.questions[int(q_num)]

    return render_template(
        "question.html",
        question=question,
        q_num=q_num,
        title=title,
        instructions=instructions,
    )


@app.route("/answer", methods=["POST"])
def post_answer():
    """Post user submitted answer to Foo DB & redirect to next question or thank you page if survey completed."""
    answer = request.form.get("answer", "")
    next_question = int(request.form.get("q_num", "")) + 1
    redirect_path = ""

    # Add too Foo DB
    responses.append(answer)

    # Determine Next Q or TY Page
    if next_question < len(satisfaction_survey.questions):
        redirect_path = f"/question/{next_question}"
    else:
        redirect_path = "/thank-you"
        flash("Survey Answers Saved", "info")

    return redirect(redirect_path)


@app.route("/thank-you")
def thank_you_page():
    return render_template("thank-you.html")
