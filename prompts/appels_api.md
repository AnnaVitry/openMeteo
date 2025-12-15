# 📚 Documentation des Appels API (services/weather_api.py)

Ce document détaille les fonctions développées pour interroger l'API Open-Meteo, conformément aux exigences du projet.

## 1. Fonction Générique : `get_forecast`

C'est la fonction fondamentale qui gère la communication avec l'API, la construction de l'URL dynamique, et la gestion des erreurs.

### Signature
```python
def get_forecast(latitude: str, longitude: str, hourly_vars: List[str]) -> Dict[str, Any]