import pytest
from app.services.matcher import match_symptoms

def test_match_migraine():
    input_symptoms = ["headache", "nausea"]
    results = match_symptoms(input_symptoms)
    matched = [name for name, _ in results]
    assert "Migraine" in matched

def test_match_cold():
    input_symptoms = ["sneezing", "runny nose"]
    results = match_symptoms(input_symptoms)
    matched = [name for name, _ in results]
    assert "Common Cold" in matched

def test_no_match():
    input_symptoms = ["unknownsymptom"]
    results = match_symptoms(input_symptoms)
    assert len(results) == 0
