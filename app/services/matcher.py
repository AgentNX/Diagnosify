import json
from pathlib import Path
import unicodedata

# Load data
data_path = Path(__file__).resolve().parent.parent.parent / "data" / "conditions.json"
with open(data_path, "r", encoding="utf-8") as f:
    CONDITIONS = json.load(f)

def normalize(text):
    # Normalize Unicode, trim, lowercase, and replace special commas
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("，", ",")  # Convert full-width comma to normal
    return text.strip().lower()

def parse_input(symptom_input):
    return [normalize(symptom) for symptom in symptom_input.split(",") if symptom.strip()]

def match_symptoms(input_symptoms, min_matches=1):
    input_set = set(parse_input(",".join(input_symptoms)))  # In case it's a list already

    results = []
    for condition in CONDITIONS:
        condition_symptoms = set(normalize(s) for s in condition["symptoms"])
        match_count = len(input_set & condition_symptoms)
        total_symptoms = len(condition_symptoms)

        # Only include results where symptoms match the minimum required number
        if match_count >= min_matches:
            results.append({
                "name": condition["name"],
                "match_count": match_count,
                "total_symptoms": total_symptoms
            })

    return sorted(results, key=lambda x: -x["match_count"])

def format_results(results):
    formatted_results = []
    for result in results:
        # Construct the "X/Y" match string
        match_text = f"{result['name']} {result['match_count']}/{result['total_symptoms']} шинж тэмдэг таарсан"
        formatted_results.append(match_text)
    return formatted_results
