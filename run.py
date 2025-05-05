# Import necessary modules for database migrations and application setup
from flask_migrate import Migrate
from app import create_app, db

# Create the Flask application instance
app = create_app()

# Initialize the Migrate extension with the app and db objects
migrate = Migrate(app, db)

# Use the app's application context to create all tables in the database
# This ensures that the database schema is created according to the models
with app.app_context():
    db.create_all()

# Start the Flask app with debugging enabled and make it accessible from any host
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# Import the SymptomLog model and db object for logging symptoms
from app.models.models import SymptomLog, db

# Function to log symptoms and their matched conditions into the database
def log_symptoms(symptoms, matched_condition):
    # Loop through the list of symptoms and create an entry for each one
    for symptom in symptoms:
        # Create a new SymptomLog entry with the symptom and matched condition
        entry = SymptomLog(symptom=symptom, matched_condition=matched_condition)
        # Add the entry to the session
        db.session.add(entry)
    
    # Commit the session to persist the changes to the database
    db.session.commit()
