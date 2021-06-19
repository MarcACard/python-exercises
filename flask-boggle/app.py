from flask import Flask, session, render_template, request, jsonify
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "FaKe_SeCrEt_KeY"
boggle_game = Boggle()


@app.route("/")
def home():
    board = boggle_game.make_board()
    session["board"] = board

    return render_template("index.html", board=board)


@app.route("/validate-guess", methods=["POST"])
def validate_guess():
    # Todo: Validate that guess exists
    guess = request.json.get("guess", "")
    result = boggle_game.check_valid_word(session["board"], guess)

    return jsonify({"result": result})
