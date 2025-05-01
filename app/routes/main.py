from flask import Blueprint, render_template, request
from app.services.matcher import match_symptoms

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        symptoms = request.form.get("symptoms", "").lower().split(",")
        results = match_symptoms(symptoms)
        return render_template("result.html", results=results, symptoms=symptoms)
    return render_template("index.html")
