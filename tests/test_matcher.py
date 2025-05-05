# This file contains unit tests for the symptom matcher functionality in the Diagnosify 
# application. The tests are designed to check whether the symptom matching logic correctly 
# identifies the medical conditions based on the input symptoms.

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pytest
from app import create_app
from app.services.matcher import *

# Create app instance for testing
app = create_app()

@pytest.fixture
def app_context():
    with app.app_context():  # Ensures the app context is active for the test
        yield

def test_match_cough(app_context):
    input_symptoms = ["хамар битүүрэх", "ханиалгах", "толгой өвдөх", "нойрмоглох"]
    results = match_symptoms(input_symptoms)
    matched = [result["name"] for result in results]
    assert "Ханиад" in matched

def test_match_flu(app_context):
    input_symptoms = ["их халуурах", "булчин өвдөх", "даарч чичрэх", "ядаргаа"]
    results = match_symptoms(input_symptoms)
    matched = [result["name"] for result in results]
    assert "Томуу" in matched

def test_match_skin_allergy(app_context):
    input_symptoms = ["загатнах", "улайлт үүсэх", "арьс хуурайших", "гүвдрүү үүсэх"]
    results = match_symptoms(input_symptoms)
    matched = [result["name"] for result in results]
    assert "Арьсны харшил" in matched

def test_match_depression(app_context):
    input_symptoms = ["урам хугарах", "унтахад хүндрэлтэй болох", "хоолны дуршил буурах", "анхаарал төвлөрөхгүй байх"]
    results = match_symptoms(input_symptoms)
    matched = [result["name"] for result in results]
    assert "Сэтгэл гутрал" in matched

def test_match_diabetes(app_context):
    input_symptoms = ["ам их цангах", "шээс их гарах", "жингээ алдах", "ядаргаа"]
    results = match_symptoms(input_symptoms)
    matched = [result["name"] for result in results]
    assert "Чихрийн шижин" in matched

def test_match_digestion_issues(app_context):
    input_symptoms = ["гэдэсний хий дүүрэх", "гүйлгэх", "хоолны дуршилгүй болох", "ходоод эвгүйрхэх"]
    results = match_symptoms(input_symptoms)
    matched = [result["name"] for result in results]
    assert "Хоол боловсруулахын асуудал" in matched

def test_match_asthma(app_context):
    input_symptoms = ["амьсгал давчдах", "цээжээр хяхтнах", "ханиалгах", "амьсадах"]
    results = match_symptoms(input_symptoms)
    matched = [result["name"] for result in results]
    assert "Астма" in matched

def test_match_cancer(app_context):
    input_symptoms = ["жингээ алдах", "урамгүй байх", "арьс толботой болох", "бие сулрах"]
    results = match_symptoms(input_symptoms)
    matched = [result["name"] for result in results]
    assert "Хорт хавдар" in matched

def test_match_hepatitis_a(app_context):
    input_symptoms = ["арьс шарлах", "шээсний өнгө бараан болох", "халуурах", "дотор муухайрах"]
    results = match_symptoms(input_symptoms)
    matched = [result["name"] for result in results]
    assert "Гепатит A" in matched

def test_match_hepatitis_b(app_context):
    input_symptoms = ["арьс шарлах", "бие сулрах", "хоолны дуршил буурах", "халуурах"]
    results = match_symptoms(input_symptoms)
    matched = [result["name"] for result in results]
    assert "Гепатит B" in matched

def test_match_hepatitis_c(app_context):
    input_symptoms = ["бие сулрах", "арьс шарлах", "хоолны дуршил буурах", "халуурах"]
    results = match_symptoms(input_symptoms)
    matched = [result["name"] for result in results]
    assert "Гепатит C" in matched

def test_match_aids(app_context):
    input_symptoms = ["бие сулрах", "халуурах", "жингээ алдах", "дархлаа сулрах"]
    results = match_symptoms(input_symptoms)
    matched = [result["name"] for result in results]
    assert "ДОХ" in matched

def test_match_hiv(app_context):
    input_symptoms = ["бие сулрах", "халуурах", "жингээ алдах", "дархлаа сулрах"]
    results = match_symptoms(input_symptoms)
    matched = [result["name"] for result in results]
    assert "ХДХВ" in matched

def test_match_anxiety(app_context):
    input_symptoms = ["сэтгэл түгших", "зүрх дэлсэх", "амьсгаадах", "анхаарал төвлөрөхгүй байх"]
    results = match_symptoms(input_symptoms)
    matched = [result["name"] for result in results]
    assert "Сэтгэл түгших эмгэг" in matched

def test_match_insomnia(app_context):
    input_symptoms = ["унтахад хүндрэлтэй", "бодох чадвар буурах", "анхаарал төвлөрөхгүй байх", "сэтгэл гутрах"]
    results = match_symptoms(input_symptoms)
    matched = [result["name"] for result in results]
    assert "Нойргүйдэл" in matched

def test_no_match(app_context):
    input_symptoms = ["танигдсангүй"]
    results = match_symptoms(input_symptoms)
    assert len(results) == 0
