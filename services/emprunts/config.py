import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/bibliotheque_emprunts')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret-key-emprunts')
    LIVRES_SERVICE_URL = os.getenv('LIVRES_SERVICE_URL', 'http://localhost:5001')
    UTILISATEURS_SERVICE_URL = os.getenv('UTILISATEURS_SERVICE_URL', 'http://localhost:5002')
