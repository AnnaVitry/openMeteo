# utils/error_handler.py

class ApiError(Exception):
    """Exception personnalisée pour les erreurs de réponse API (status 4xx ou 5xx)."""
    def __init__(self, status_code, message="Erreur de l'API Open-Meteo"):
        self.status_code = status_code
        self.message = f"{message} (Statut: {status_code})"
        super().__init__(self.message)

class NetworkError(Exception):
    """Exception personnalisée pour les problèmes réseau ou les timeouts."""
    pass

def handle_api_error(response):
    """
    Vérifie le statut de la réponse et lève l'exception appropriée.
    """
    if response.status_code >= 400:
        try:
            # Tente de décoder le message d'erreur JSON du corps de la réponse
            error_data = response.json()
            reason = error_data.get("reason", "Raison non spécifiée")
            message = f"Échec de la requête API. Erreur: {reason}"
        except:
            # Si la réponse n'est pas en JSON
            message = f"Échec de la requête API. Réponse non JSON."
            
        raise ApiError(response.status_code, message)