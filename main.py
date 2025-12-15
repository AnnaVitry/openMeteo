# main.py

from config.settings import settings
from services.weather_api import get_forecast
from utils.error_handler import ApiError, NetworkError
import json

def main():
    """Point d'entrée principal de l'application."""
    
    lat = settings.DEFAULT_LATITUDE
    lon = settings.DEFAULT_LONGITUDE
    
    if not settings.BASE_URL:
        print("Erreur de configuration : OPENMETEO_BASE_URL n'est pas défini dans .env.")
        return

    print(f"🌍 Requête de prévisions pour la Réunion (Lat: {lat}, Lon: {lon})")
    print("-" * 50)
    
    try:
        # 1. Appel de la fonction API (gérée dans services/weather_api.py)
        forecast_data = get_forecast(lat, lon)
        
        # 2. Traitement des données
        print("✅ Données reçues avec succès.")
        
        # Afficher les 5 premières heures pour la démo
        hourly_data = forecast_data.get("hourly", {})
        times = hourly_data.get("time", [])[:5]
        pressures = hourly_data.get("surface_pressure", [])[:5]
        winds = hourly_data.get("wind_gusts_10m", [])[:5]
        
        print("\nPrévisions pour les 5 prochaines heures:")
        for t, p, w in zip(times, pressures, winds):
            print(f"  Heure: {t} | Pression: {p} hPa | Rafales: {w} km/h")
        
        print("\nDonnées JSON complètes (extrait):")
        print(json.dumps(forecast_data, indent=2)[:500] + "...") # Afficher un extrait

    except ApiError as e:
        print(f"❌ Erreur de l'API : {e.message}")
    except NetworkError as e:
        print(f"❌ Erreur de réseau : {e}")
    except Exception as e:
        print(f"❌ Une erreur inattendue s'est produite : {e}")

if __name__ == "__main__":
    main()