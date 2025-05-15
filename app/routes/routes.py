from flask import Blueprint, render_template, request
from app.services.matcher import match_symptoms
from app.models.models import db, SymptomLog

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        symptoms_input = request.form.get("symptoms", "")
        symptoms = symptoms_input.lower().split(",")
        results = match_symptoms(symptoms)

        for result in results:
            matched_symptoms = result.get("matched_symptoms", [])
            if matched_symptoms:
                log = SymptomLog(
                    symptom=symptoms_input,
                    matched_condition=result.get("condition", "Unknown")
                )
                db.session.add(log)
        db.session.commit()

        return render_template("result.html", results=results, symptoms=symptoms)

    return render_template("index.html")

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/services')
def services():
    return render_template('services.html')

@main.route('/faq')
def faq():
    return render_template('faq.html')

@main.route('/feedback')
def feedback():
    return render_template('feedback.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')
