import json
import unicodedata
from pathlib import Path

# 🧠 For database logging
from app import db
from app.models.models import SymptomLog  # Ensure your model is defined here

# 📁 Load condition data from JSON
# This path points to the conditions.json file which contains the predefined conditions and their associated symptoms
data_path = Path(__file__).resolve().parent.parent.parent / "data" / "conditions.json"
with open(data_path, "r", encoding="utf-8") as f:
    CONDITIONS = json.load(f)

def normalize(text):
    """
    Normalize and clean the input text for comparison.
    
    Args:
        text (str): Input text to normalize.

    Returns:
        str: Normalized and cleaned text.
    """
    text = unicodedata.normalize("NFKC", text)  # Normalize text using Unicode NFKC form
    text = text.replace("，", ",")  # Handle full-width commas (from languages like Chinese)
    return text.strip().lower()  # Remove extra spaces and convert to lowercase

def parse_input(symptom_input):
    """
    Parse and normalize a list of symptoms input by the user.
    
    Args:
        symptom_input (str): A string containing comma-separated symptoms.

    Returns:
        list: A list of normalized symptoms.
    """
    return [normalize(symptom) for symptom in symptom_input.split(",") if symptom.strip()]

def match_symptoms(input_symptoms, min_matches=1):
    """
    Match user-inputted symptoms against predefined conditions and return results.
    
    Args:
        input_symptoms (list or str): A list or string of symptoms input by the user.
        min_matches (int): The minimum number of symptom matches required to consider a condition as a match.

    Returns:
        list: A list of matched conditions, sorted by the number of matched symptoms.
    """
    input_set = set(parse_input(",".join(input_symptoms)))  # Ensure input is treated as a list and normalized

    results = []
    # Loop through all the predefined conditions and compare symptoms
    for condition in CONDITIONS:
        condition_symptoms = set(normalize(s) for s in condition["symptoms"])  # Normalize each symptom of the condition
        match_count = len(input_set & condition_symptoms)  # Count the number of matching symptoms
        total_symptoms = len(condition_symptoms)

        # Only include conditions that meet the minimum match criteria
        if match_count >= min_matches:
            results.append({
                "name": condition["name"],  # Condition name
                "match_count": match_count,  # Number of matched symptoms
                "total_symptoms": total_symptoms  # Total symptoms in the condition's set
            })

    # Sort results by the number of matches in descending order
    sorted_results = sorted(results, key=lambda x: -x["match_count"])

    # ✅ Log the top result to the database if any matches were found
    if sorted_results:
        try:
            top_match = sorted_results[0]
            # Create a new log entry with the user input and matched condition
            log = SymptomLog(
                symptom=", ".join(input_symptoms),
                matched_condition=top_match["name"]
            )
            db.session.add(log)  # Add the log to the database session
            db.session.commit()  # Commit the changes to the database
        except Exception as e:
            db.session.rollback()  # Rollback in case of any errors
            print("❌ Database Error:", e)

    return sorted_results  # Return the sorted list of results

def format_results(results):
    """
    Format the results to make them user-friendly.
    
    Args:
        results (list): A list of matched results with condition names and match counts.

    Returns:
        list: A list of formatted result strings.
    """
    formatted_results = []
    for result in results:
        # Format the result into a string that is easier to read for the user
        match_text = f"{result['name']} {result['match_count']}/{result['total_symptoms']} шинж тэмдэг таарсан"
        formatted_results.append(match_text)
    return formatted_results
