# services/weather_api.py

import requests
from typing import Dict, Any, List
from config.settings import settings
from utils.error_handler import handle_api_error, NetworkError, ApiError

def _validate_coordinates(latitude: str, longitude: str):
    """
    Validation simple de la plage de latitude et de longitude.
    Les coordonnées de la Réunion (-20.89, 55.45) servent de référence.
    """
    try:
        lat = float(latitude)
        lon = float(longitude)
        
        # Vérification des plages standard (ajustées pour les environnements tropicaux)
        if not (-90.0 <= lat <= 90.0 and -180.0 <= lon <= 180.0):
            raise ValueError("Latitude ou longitude hors de la plage valide.")
            
    except ValueError:
        raise ValueError("Les coordonnées doivent être des valeurs numériques valides.")

def get_forecast(latitude: str, longitude: str, hourly_vars: List[str]) -> Dict[str, Any]:
    """
    Appel générique à l'endpoint de prévision Open-Meteo.
    
    L'URL est construite dynamiquement en utilisant settings.BASE_URL.
    
    :param latitude: Latitude de la zone.
    :param longitude: Longitude de la zone.
    :param hourly_vars: Liste des variables météo horaires à récupérer (ex: ['pressure_msl', 'wind_speed_10m']).
    :return: Le dictionnaire JSON de la réponse API.
    :raises NetworkError: En cas de problème de connexion.
    :raises ApiError: En cas d'erreur côté serveur (4xx/5xx).
    :raises ValueError: En cas de coordonnées invalides.
    """
    # 1. Validation des paramètres
    _validate_coordinates(latitude, longitude)
    
    # 2. Construction de l'URL dynamique et des paramètres météo
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": ",".join(hourly_vars), # Convertit la liste en chaîne de caractères séparée par des virgules
        "models": "meteofrance_seamless",  # Modèle Météo-France
        "timezone": "auto",
        "forecast_days": 7  # Prévisions sur 7 jours
    }
    
    print(f"DEBUG: Requête à {settings.BASE_URL} avec {len(hourly_vars)} variables.")
    
    try:
        # 3. Appel API et gestion des erreurs réseau
        response = requests.get(settings.BASE_URL, params=params, timeout=15)
        
        # 4. Gestion des erreurs 4xx/5xx
        handle_api_error(response)
        
        # 5. Parsing des réponses (Conversion implicite du JSON par requests.json())
        return response.json()
    
    except requests.exceptions.Timeout:
        raise NetworkError("La requête a expiré après 15 secondes. Problème réseau ou serveur surchargé.")
    except requests.exceptions.RequestException as e:
        # Capturer les autres erreurs de connexion (DNS, SSL, etc.)
        raise NetworkError(f"Une erreur de connexion s'est produite: {e}")

# --- Fonctions d'appel spécifiques (pour la cohérence du livrable) ---

def get_wind_data(latitude: str, longitude: str) -> Dict[str, Any]:
    """Récupère les données de vent (vitesse et rafales)."""
    return get_forecast(
        latitude, 
        longitude, 
        hourly_vars=['wind_speed_10m', 'wind_gusts_10m']
    )

def get_pressure_msl_data(latitude: str, longitude: str) -> Dict[str, Any]:
    """Récupère la pression au niveau de la mer (msl)."""
    return get_forecast(
        latitude, 
        longitude, 
        hourly_vars=['pressure_msl']
    )

def get_cyclone_variables(latitude: str, longitude: str) -> Dict[str, Any]:
    """Récupère toutes les variables critiques pour la surveillance cyclone."""
    return get_forecast(
        latitude, 
        longitude, 
        hourly_vars=['surface_pressure', 'wind_speed_10m', 'wind_gusts_10m', 'precipitation', 'cape']
    )

# Mettez à jour main.py pour utiliser get_cyclone_variables pour tester toutes les fonctions.