from flask import Flask, render_template, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "FaKe_SeCrEt_KeY"
toolbar = DebugToolbarExtension(app)


@app.route("/")
def home():
    return render_template("index.html", survey=satisfaction_survey, is_index=True)


@app.route("/start-session", methods=["POST"])
def start_session():
    session["responses"] = []
    return redirect("/question/0")


@app.route("/question/<int:q_num>")
def survey_question(q_num):
    """Render Survey Questions to user. Current functionality will prevent users from retaking the survery or accessing previous questions."""
    responses = session["responses"]

    if len(responses) == len(satisfaction_survey.questions):
        # Survey is completed
        return redirect("/thank-you")

    if len(responses) != q_num:
        flash(
            "Attempted to access invalid question, or question already answered",
            "error",
        )
        return redirect(f"/question/{len(responses)}")

    # Render survey question info
    question = satisfaction_survey.questions[q_num]

    return render_template(
        "question.html", survey=satisfaction_survey, question=question, q_num=q_num
    )


@app.route("/answer", methods=["POST"])
def post_answer():
    """Post user submitted answer to user session & redirect to next question or thank you page if survey completed."""
    answer = request.form.get("answer", "")

    # Add user answer to their session
    responses = session["responses"]
    responses.append(answer)
    session["responses"] = responses

    # Determine Next Q or TY Page
    if len(responses) < len(satisfaction_survey.questions):
        return redirect(f"/question/{len(responses)}")
    else:
        return redirect("/thank-you")


@app.route("/thank-you")
def thank_you_page():
    return render_template("thank-you.html", survey=satisfaction_survey)
