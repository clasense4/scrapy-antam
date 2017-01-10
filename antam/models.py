import settings
from orator import DatabaseManager

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns orator engine instance
    """
    return DatabaseManager(settings.DATABASES)
