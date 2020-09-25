from flask import Blueprint, render_template

# Creating the blueprint and giving it static and template folders to reference
bluprnt = Blueprint(
    "blueprnt", __name__, static_folder="static", template_folder="templates"
)


@bluprnt.route("/blu")
@bluprnt.route("/")
def blu():
    """

    :return: test blueprint
    """
    return render_template("blueTest.html")
