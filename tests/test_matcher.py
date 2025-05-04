import pytest
from app.services.matcher import match_symptoms

def test_match_migraine():
    input_symptoms = ["хамар битүүрэх", "ханиалгах", "толгой өвдөх", "нойрмоглох"]
    results = match_symptoms(input_symptoms)
    matched = [name for name, _ in results]
    assert "Ханиад" in matched

def test_match_cold():
    input_symptoms = ["их халуурах", "булчин өвдөх", "даарч чичрэх", "ядаргаа"]
    results = match_symptoms(input_symptoms)
    matched = [name for name, _ in results]
    assert "Томуу" in matched

def test_no_match():
    input_symptoms = ["танигдсангүй"]
    results = match_symptoms(input_symptoms)
    assert len(results) == 0
