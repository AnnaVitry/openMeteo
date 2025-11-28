# services/weather_api.py

import requests
from config.settings import settings
from utils.error_handler import handle_api_error, NetworkError
from typing import Dict, Any

def get_forecast(latitude: str, longitude: str) -> Dict[str, Any]:
    """
    Appelle l'endpoint de prévision Open-Meteo pour les coordonnées données.
    
    :param latitude: Latitude de la zone.
    :param longitude: Longitude de la zone.
    :return: Le dictionnaire JSON de la réponse API.
    """
    # Variables critiques pour la surveillance cyclone (comme dans la doc précédente)
    hourly_vars = "surface_pressure,wind_speed_10m,wind_gusts_10m,precipitation,cape"
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": hourly_vars,
        "models": "meteofrance_seamless",  # Utilisation du modèle Météo-France
        "timezone": "auto",
        "forecast_days": 3 # Prévisions sur 3 jours pour la démo
    }
    
    try:
        # Envoi de la requête GET
        response = requests.get(settings.BASE_URL, params=params, timeout=10)
        
        # Gestion des erreurs HTTP (4xx, 5xx)
        handle_api_error(response)
        
        # Si le statut est 200 OK
        return response.json()
    
    except requests.exceptions.Timeout:
        raise NetworkError("La requête a expiré après 10 secondes. Problème réseau ou serveur surchargé.")
    except requests.exceptions.RequestException as e:
        raise NetworkError(f"Une erreur de connexion s'est produite: {e}")