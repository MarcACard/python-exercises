from flask import Flask, request
from operations import *

app = Flask(__name__)


@app.route("/add")
def get_add():
    a = int(request.args.get("a", ""))
    b = int(request.args.get("b", ""))

    return str(add(a, b))


@app.route("/sub")
def get_sub():
    a = int(request.args.get("a", ""))
    b = int(request.args.get("b", ""))

    return str(sub(a, b))


@app.route("/mult")
def get_mult():
    a = int(request.args.get("a", ""))
    b = int(request.args.get("b", ""))

    return str(mult(a, b))


@app.route("/div")
def get_div():
    a = int(request.args.get("a", ""))
    b = int(request.args.get("b", ""))

    return str(div(a, b))


# Further Study
# -------------
operations = {"add": add, "sub": sub, "mult": mult, "div": div}


@app.route("/math/<operator>")
def get_result(operator):
    """Get the result of a & b based on the operator route used."""

    a = int(request.args.get("a", ""))
    b = int(request.args.get("b", ""))

    return str(operations[operator](a, b))
