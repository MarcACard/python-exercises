from flask import Flask, session, render_template, request, jsonify
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "FaKe_SeCrEt_KeY"
boggle_game = Boggle()


@app.route("/")
def home():
    """Return homepage to user and set/load user session data."""
    board = boggle_game.make_board()
    session["board"] = board
    stats = session.get("stats", {"games_played": 0, "highscore": 0})
    session["stats"] = stats

    return render_template("index.html", board=board, stats=stats)


@app.route("/validate-guess", methods=["POST"])
def validate_guess():
    """Validate users submitted word and return json repsonse with results."""
    guess = request.json.get("guess", "")
    result = boggle_game.check_valid_word(session["board"], guess)

    return jsonify({"result": result})


@app.route("/score-game", methods=["POST"])
def score_game():
    """Update user stats and determine if user broke their high score."""
    score = request.json.get("score", "")
    stats = session["stats"]
    newHighscore = False

    # Update user Metrics
    stats["games_played"] = stats["games_played"] + 1
    if score > stats["highscore"]:
        stats["highscore"] = score
        newHighscore = True

    session["stats"] = stats

    return jsonify({"stats": stats, "new_highscore": newHighscore})
