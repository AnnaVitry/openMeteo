# config/settings.py

import os
from dotenv import load_dotenv

# Charge les variables d'environnement du fichier .env
load_dotenv()

class Settings:
    """Stocke toutes les configurations de l'application."""
    
    # Lecture des variables du .env
    BASE_URL = os.getenv("OPENMETEO_BASE_URL")
    
    DEFAULT_LATITUDE = os.getenv("DEFAULT_LATITUDE")
    DEFAULT_LONGITUDE = os.getenv("DEFAULT_LONGITUDE")
    
    API_KEY = os.getenv("OPENMETEO_API_KEY") # Pour référence, même si non utilisée ici

# Créez une instance de Settings pour l'utiliser dans le reste de l'application
settings = Settings()