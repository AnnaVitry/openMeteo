# 🌊 Project Open-Meteo | Surveillance Météo (Réunion - Météo-France)

---

## 📌 1. Introduction

Ce projet implémente un client Python pour l'API Open-Meteo, ciblant spécifiquement la récupération des données du modèle **Météo-France Seamless** pour la zone de l'Île de la Réunion. Il est conçu avec une architecture propre, utilisant les meilleures pratiques (gestion des erreurs, configuration centralisée, appels API séparés).

L'objectif est de récupérer les variables critiques pour la **surveillance des systèmes cycloniques**.

---

## 🏗️ 2. Architecture du Projet

Le projet est organisé en modules pour séparer clairement les responsabilités (Séparation des préoccupations).

```bash
    project_openmeteo/
    ├── .env                  # Configuration (Clés API, URL de base)
    ├── main.py               # Point d'entrée de l'application
    ├── services/             # Fonctions d'appel API spécifiques
    │   └── weather_api.py
    ├── config/               # Gestion des variables d'environnement
    │   └── settings.py
    └── utils/                # Fonctions utilitaires (Gestion des erreurs)
    │   └── error_handler.py
    └── prompts/
        └── squelette.md     # Documenter les prompts utilisés
        └── generer-du-code-avec-llm-brief-2.pdf # Instructions de Brief
        └── meteo.md         # Phase 1 du projet (familiarisation API OpenMeteo)
```

---

## ⚙️ 3. Installation et Configuration

### 3.1. Prérequis

Vous devez avoir Python (3.8+) installé sur votre système.

### 3.2. Installation des Dépendances

Installez les librairies nécessaires via `pip` :

```bash
pip install requests python-dotenv
```

### 3.3. Configuration du fichier .env
Créez le fichier .env à la racine du projet et remplissez les variables. Le système utilisera les coordonnées de la Réunion par défaut.

```Ini, TOML
# .env
# URL de base pour l'API de prévisions
OPENMETEO_BASE_URL="[https://api.open-meteo.com/v1/forecast](https://api.open-meteo.com/v1/forecast)"

# Coordonnées par défaut de l'Île de la Réunion (Saint-Denis)
DEFAULT_LATITUDE="-20.89"
DEFAULT_LONGITUDE="55.45"
```

## 🚀 4. Exécution

Exécutez l'application à partir du répertoire racine du projet :
```Bash
python main.py
```
Le script affichera un aperçu des données horaires de pression et de vent.

---

## 5. 📚 Documentation de l'Endpoint
### 5.1. Endpoint de Prévisions

| Élément | Valeur | Rôle dans la Requête |
| :--- | :--- | :--- |
| **Méthode HTTP** | `GET` | Récupération des données. |
| **Endpoint de Base** | `https://api.open-meteo.com/v1/forecast` | Adresse principale de l'API. |
| **Modèle utilisé** | `models=meteofrance_seamless` | Modèle Météo-France à haute résolution. |

### 5.2. Variables Clés pour la Surveillance Cyclonique (hourly=...)

| Variable            | Unité de Réponse (Par Défaut) | Importance pour la Surveillance Cyclonique                                                                 |
|---------------------|------------------------------|-----------------------------------------------------------------------------------------------------------|
| **wind_gusts_10m**      | `km/h`                         | **Alerte**: Rafales maximales de vent, indicateur direct des dommages potentiels.                  |
| **wind_speed_10m**     | `km/h`                         | **Classification**: Vitesse moyenne du vent pour la catégorisation du système (Dépression, Tempête Tropicale, Cyclone). |
| **surface_pressure**    | `hPa` (Hectopascals)           | **Intensification**: Une chute rapide ou une valeur basse (souvent sous 1000 hPa) signale un creusement et un renforcement du système. |
| **precipitation**       | `mm`                           | **Risque**: Quantité de pluie par heure (pour l'alerte inondation).                                           |
| **cape**                | `J/kg`                         | **Potentiel Convectif**: Indique l'énergie disponible pour les orages et l'instabilité (favorise le développement du cyclone). |

### Paramètres

| Paramètre      | Type        | Description                                                        |
|----------------|-------------|--------------------------------------------------------------------|
| latitude       | str         | Latitude du lieu.                                                  |
| longitude      | str         | Longitude du lieu.                                                 |
| hourly_vars    | List[str]   | Liste des variables météo à récupérer (ex : `['pressure_msl', 'wind_speed_10m']`). |

### 5.3. Gestion des Erreurs

La gestion des erreurs est centralisée dans `utils/error_handler.py`:

- `ApiError` **(4xx/5xx)** : 
  - Levée si le serveur répond avec une erreur HTTP (paramètre invalide, non trouvé).
  
- `NetworkError` : 
  - Levée pour les problèmes de connexion (timeouts, requêtes échouées).

