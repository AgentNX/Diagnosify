from flask import Blueprint, render_template, request
from app.services.matcher import match_symptoms
from app.models.models import db, SymptomLog

# Create a blueprint instance for handling routes related to the application's main functionality.
main = Blueprint("main", __name__)

# Define a route for the homepage ("/"), supporting both GET and POST methods.
@main.route("/", methods=["GET", "POST"])
def index():
    # Handle POST requests when user submits symptoms
    if request.method == "POST":
        # Retrieve symptoms input from the form, and convert them to lowercase and split by commas
        symptoms_input = request.form.get("symptoms", "")
        symptoms = symptoms_input.lower().split(",")
        
        # Match symptoms using a custom matcher service
        results = match_symptoms(symptoms)

        # Iterate over the results and log matched symptoms in the database
        for result in results:
            matched_symptoms = result.get("matched_symptoms", [])  # Safely get matched symptoms
            if matched_symptoms:  # Check if matched_symptoms list is not empty
                log = SymptomLog(
                    symptom=symptoms_input,  # Log the user's symptoms
                    matched_condition=result.get("condition", "Unknown")  # Safely access the condition, default to "Unknown"
                )
                # Add the log entry to the session
                db.session.add(log)

        # Commit the session to save changes to the database
        db.session.commit()

        # Render the results page with the matched symptoms and input symptoms
        return render_template("result.html", results=results, symptoms=symptoms)

    # Render the index page if the request is a GET request (i.e., initial page load)
    return render_template("index.html")
