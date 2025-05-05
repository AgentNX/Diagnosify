# This file defines the database model for the 'SymptomLog' table using SQLAlchemy.
# It contains the definition of the SymptomLog class, which maps to the 'symptom_log' table in the database.
# The class also defines the structure of the table with columns and their respective data types.

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

# Initialize the SQLAlchemy object for ORM operations
db = SQLAlchemy()

class SymptomLog(db.Model):
    """
    SymptomLog class represents a record in the symptom_log table.
    It holds information about the symptoms reported by users and the matched conditions.

    Attributes:
        id (int): The unique identifier for the symptom log entry.
        symptom (str): The symptom reported by the user.
        matched_condition (str): The condition matched to the symptom.
        timestamp (datetime): The timestamp when the record was created, stored in UTC timezone.
    """

    # Unique identifier for each symptom log entry
    id = db.Column(db.Integer, primary_key=True)

    # The symptom reported by the user
    symptom = db.Column(db.String(120))

    # The condition matched to the symptom
    matched_condition = db.Column(db.String(120))

    # Timestamp of the entry, stored in UTC timezone by default
    timestamp = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
