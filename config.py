import os

class Config:
    """
    - URI for connecting to the PostgreSQL database.
    - Retrieves the value from the environment variable 'DATABASE_URL'. 
    - If it's not set, defaults to 'postgresql://user:pass@db:5432/symptoms'.
    - Format: postgresql://username:password@hostname:port/database_name
    """
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:pass@db:5432/symptoms")
    """
    - Disables Flask-SQLAlchemy's modification tracking to improve performance.
    - It reduces unnecessary overhead by not tracking changes to database objects.
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    """
    - Secret key used for securely signing cookies and managing sessions.
    - Retrieves the value from the environment variable 'SECRET_KEY'.
    - If not set, defaults to 'super-secret-key'.
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'super-secret-key')