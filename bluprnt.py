from flask import Blueprint, render_template

bluprnt = Blueprint("blueprnt", __name__, static_folder="static", template_folder="template")

@bluprnt.route("/blu")
@bluprnt.route("/")
def blu():
    return render_template("blueTest.html")