# 🌪️ Documentation d'Endpoint pour la Détection de Cyclone (Open-Meteo)

Cette documentation décrit l'utilisation de l'API Open-Meteo avec les paramètres spécifiques au modèle Météo-France (`meteofrance_seamless`) pour la surveillance des systèmes cycloniques dans la zone de l'Océan Indien.

## 1. 🌐 Endpoint et Configuration de Base

L'API Open-Meteo utilise le point d'accès de prévision standard pour toutes les requêtes météo.

| Élément | Valeur | Rôle dans la Requête |
| :--- | :--- | :--- |
| **Méthode HTTP** | `GET` | Pour la récupération de données. |
| **Endpoint de Base** | `https://api.open-meteo.com/v1/forecast` | L'adresse de l'API de prévisions. |
| **Modèle** | `models=meteofrance_seamless` | **Crucial :** Spécifie l'utilisation du modèle Météo-France pour la haute résolution. |
| **Coordonnées** | `latitude=LATITUDE & longitude=LONGITUDE` | À remplacer par les coordonnées de la zone à surveiller (ex: La Réunion). |

## 2. 📋 Variables Horaires Clés (`hourly=...`)

Pour la détection et la surveillance d'un cyclone, les variables suivantes sont essentielles. Elles doivent être incluses dans le paramètre `hourly`.

| Variable | Unité de Réponse (Par Défaut) | Importance pour la Surveillance Cyclonique |
| :--- | :--- | :--- |
| **`wind_gusts_10m`** | `km/h` | **Alerte Immédiate.** Rafales maximales de vent, indicateur direct des dommages potentiels. |
| **`wind_speed_10m`** | `km/h` | **Classification.** Vitesse moyenne du vent, utilisée pour déterminer la catégorie du système cyclonique. |
| **`surface_pressure`** | `hPa` (Hectopascals) | **Intensification.** Une **chute rapide** ou une **valeur basse** (souvent sous 1000 hPa) signale un creusement et un renforcement du système. |
| **`precipitation`** | `mm` | **Risque d'Inondation.** Quantité de pluie par heure, essentielle pour l'alerte aux inondations. |
| **`cape`** | `J/kg` | **Potentiel Convectif.** Indique l'énergie disponible pour le développement d'orages intenses, composante des bandes de pluie cycloniques. |

## 3. 🛠️ Exemple de Requête Optimisée

Exemple utilisant les coordonnées de Saint-Denis, La Réunion (Lat: -20.89, Lon: 55.45) :
```json
GET https://api.open-meteo.com/v1/forecast?latitude=-20.89&longitude=55.45&models=meteofrance_seamless&hourly=surface_pressure,wind_speed_10m,wind_gusts_10m,precipitation,cape&timezone=auto

{"latitude":-21.25,"longitude":55.25,"generationtime_ms":0.09870529174804688,"utc_offset_seconds":14400,"timezone":"Indian/Reunion","timezone_abbreviation":"GMT+4","elevation":42.0,"hourly_units":{"time":"iso8601","surface_pressure":"hPa","wind_speed_10m":"km/h","wind_gusts_10m":"km/h","precipitation":"mm","cape":"J/kg"},"hourly":{"time":["2025-11-24T00:00","2025-11-24T01:00","2025-11-24T02:00","2025-11-24T03:00","2025-11-24T04:00","2025-11-24T05:00","2025-11-24T06:00","2025-11-24T07:00","2025-11-24T08:00","2025-11-24T09:00","2025-11-24T10:00","2025-11-24T11:00","2025-11-24T12:00","2025-11-24T13:00","2025-11-24T14:00","2025-11-24T15:00","2025-11-24T16:00","2025-11-24T17:00","2025-11-24T18:00","2025-11-24T19:00","2025-11-24T20:00","2025-11-24T21:00","2025-11-24T22:00","2025-11-24T23:00","2025-11-25T00:00","2025-11-25T01:00","2025-11-25T02:00","2025-11-25T03:00","2025-11-25T04:00","2025-11-25T05:00","2025-11-25T06:00","2025-11-25T07:00","2025-11-25T08:00","2025-11-25T09:00","2025-11-25T10:00","2025-11-25T11:00","2025-11-25T12:00","2025-11-25T13:00","2025-11-25T14:00","2025-11-25T15:00","2025-11-25T16:00","2025-11-25T17:00","2025-11-25T18:00","2025-11-25T19:00","2025-11-25T20:00","2025-11-25T21:00","2025-11-25T22:00","2025-11-25T23:00","2025-11-26T00:00","2025-11-26T01:00","2025-11-26T02:00","2025-11-26T03:00","2025-11-26T04:00","2025-11-26T05:00","2025-11-26T06:00","2025-11-26T07:00","2025-11-26T08:00","2025-11-26T09:00","2025-11-26T10:00","2025-11-26T11:00","2025-11-26T12:00","2025-11-26T13:00","2025-11-26T14:00","2025-11-26T15:00","2025-11-26T16:00","2025-11-26T17:00","2025-11-26T18:00","2025-11-26T19:00","2025-11-26T20:00","2025-11-26T21:00","2025-11-26T22:00","2025-11-26T23:00","2025-11-27T00:00","2025-11-27T01:00","2025-11-27T02:00","2025-11-27T03:00","2025-11-27T04:00","2025-11-27T05:00","2025-11-27T06:00","2025-11-27T07:00","2025-11-27T08:00","2025-11-27T09:00","2025-11-27T10:00","2025-11-27T11:00","2025-11-27T12:00","2025-11-27T13:00","2025-11-27T14:00","2025-11-27T15:00","2025-11-27T16:00","2025-11-27T17:00","2025-11-27T18:00","2025-11-27T19:00","2025-11-27T20:00","2025-11-27T21:00","2025-11-27T22:00","2025-11-27T23:00","2025-11-28T00:00","2025-11-28T01:00","2025-11-28T02:00","2025-11-28T03:00","2025-11-28T04:00","2025-11-28T05:00","2025-11-28T06:00","2025-11-28T07:00","2025-11-28T08:00","2025-11-28T09:00","2025-11-28T10:00","2025-11-28T11:00","2025-11-28T12:00","2025-11-28T13:00","2025-11-28T14:00","2025-11-28T15:00","2025-11-28T16:00","2025-11-28T17:00","2025-11-28T18:00","2025-11-28T19:00","2025-11-28T20:00","2025-11-28T21:00","2025-11-28T22:00","2025-11-28T23:00","2025-11-29T00:00","2025-11-29T01:00","2025-11-29T02:00","2025-11-29T03:00","2025-11-29T04:00","2025-11-29T05:00","2025-11-29T06:00","2025-11-29T07:00","2025-11-29T08:00","2025-11-29T09:00","2025-11-29T10:00","2025-11-29T11:00","2025-11-29T12:00","2025-11-29T13:00","2025-11-29T14:00","2025-11-29T15:00","2025-11-29T16:00","2025-11-29T17:00","2025-11-29T18:00","2025-11-29T19:00","2025-11-29T20:00","2025-11-29T21:00","2025-11-29T22:00","2025-11-29T23:00","2025-11-30T00:00","2025-11-30T01:00","2025-11-30T02:00","2025-11-30T03:00","2025-11-30T04:00","2025-11-30T05:00","2025-11-30T06:00","2025-11-30T07:00","2025-11-30T08:00","2025-11-30T09:00","2025-11-30T10:00","2025-11-30T11:00","2025-11-30T12:00","2025-11-30T13:00","2025-11-30T14:00","2025-11-30T15:00","2025-11-30T16:00","2025-11-30T17:00","2025-11-30T18:00","2025-11-30T19:00","2025-11-30T20:00","2025-11-30T21:00","2025-11-30T22:00","2025-11-30T23:00"],"surface_pressure":[1012.0,1011.5,1011.1,1011.0,1010.6,1011.0,1011.6,1012.4,1012.7,1013.0,1013.2,1013.2,1012.9,1012.6,1012.2,1011.9,1011.9,1011.9,1012.2,1012.6,1013.2,1013.3,1013.5,1013.2,1012.6,1012.0,1011.7,1011.7,1011.6,1011.6,1012.2,1012.9,1012.9,1013.0,1013.2,1013.2,1012.8,1012.3,1011.7,1011.4,1011.4,1011.5,1011.9,1012.3,1012.8,1013.3,1013.7,1013.4,1012.8,1011.9,1011.3,1011.1,1011.1,1011.4,1012.0,1012.4,1012.6,1012.8,1012.7,1012.3,1011.7,1011.2,1010.9,1010.6,1010.5,1010.7,1011.2,1011.8,1012.4,1013.1,1013.3,1012.9,1012.0,1011.3,1010.8,1010.4,1010.3,1010.6,1011.2,1011.7,1011.9,1012.1,1012.0,1011.7,1011.2,1010.7,1010.2,1009.8,1009.5,1009.6,1009.9,1010.2,1010.6,1011.1,1011.2,1010.8,1010.1,1009.4,1008.8,1008.3,1008.2,1008.7,1009.5,1010.1,1010.3,1010.2,1010.2,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"wind_speed_10m":[4.0,4.4,4.1,2.3,5.6,3.2,0.8,0.8,1.6,2.9,4.2,5.8,6.1,5.4,4.7,5.4,7.5,9.2,9.2,8.4,6.9,6.7,6.5,6.3,6.0,6.2,6.2,6.9,7.2,6.1,5.1,3.8,3.3,4.0,7.7,9.4,10.5,11.1,10.8,10.5,11.5,12.8,13.2,12.5,10.1,8.2,8.8,9.2,8.6,7.8,6.6,6.1,4.9,3.1,1.0,1.1,3.0,5.0,6.3,7.1,8.0,8.7,8.0,6.6,5.5,5.1,6.0,6.9,7.1,6.6,6.1,5.1,4.1,3.5,3.4,3.5,3.9,4.6,5.2,5.0,3.1,2.7,4.3,5.4,7.6,9.6,9.7,9.3,8.5,8.5,8.6,7.4,4.0,1.1,4.1,6.2,7.7,8.2,7.6,6.7,4.8,1.8,2.4,4.1,2.9,3.5,6.1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"wind_gusts_10m":[7.2,7.2,7.2,5.8,3.6,7.9,5.0,0.7,3.6,5.0,7.2,10.1,11.2,11.2,9.7,8.6,12.6,14.0,14.0,14.0,12.2,10.1,10.1,9.7,9.0,9.0,9.4,10.4,11.2,11.2,8.3,7.2,6.5,7.6,12.6,15.1,16.9,18.0,17.6,17.6,17.6,18.7,19.1,19.1,17.6,14.4,12.2,13.0,12.6,12.6,9.7,9.0,8.3,5.8,3.2,2.2,4.0,7.6,10.8,13.0,15.1,15.8,14.8,13.0,11.2,10.4,10.4,10.1,9.7,9.4,9.0,8.6,8.3,7.9,7.2,6.8,6.5,6.8,7.9,8.6,9.0,9.0,9.7,11.9,14.8,16.6,16.9,16.2,15.5,15.1,14.8,13.7,11.5,8.6,7.2,8.6,11.5,13.3,13.0,11.9,10.4,9.4,8.3,7.9,8.6,9.7,10.8,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"precipitation":[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.10,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"cape":[300.0,180.0,120.0,80.0,410.0,350.0,300.0,260.0,290.0,310.0,340.0,360.0,400.0,390.0,320.0,210.0,160.0,100.0,60.0,20.0,10.0,10.0,10.0,10.0,10.0,20.0,30.0,40.0,30.0,10.0,10.0,0.0,0.0,0.0,0.0,10.0,10.0,10.0,10.0,0.0,0.0,0.0,0.0,0.0,10.0,20.0,30.0,30.0,30.0,10.0,10.0,0.0,0.0,0.0,0.0,0.0,0.0,10.0,10.0,20.0,30.0,30.0,30.0,20.0,10.0,10.0,10.0,10.0,10.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,10.0,10.0,10.0,10.0,10.0,10.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,10.0,10.0,10.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null]}}
```

## 4. 📝 Ce que Renvoie l'URL (Sortie JSON)

La requête renvoie un unique fichier au format **JSON (JavaScript Object Notation)**.

### Structure du Fichier JSON :

1.  **`hourly_units`**: Dictionnaire définissant l'unité de mesure pour chaque variable (ex: `"surface_pressure": "hPa"`).
2.  **`hourly`**: Dictionnaire contenant des tableaux de données.
    * Chaque clé est une variable demandée (ex: `wind_gusts_10m`).
    * La valeur est une liste chronologique de valeurs prévues (ex: `[55.2, 58.0, 61.1, ... ]`).
    * Le tableau `time` permet d'indexer chaque valeur à une date et heure précise.

---

# 📚 Documentation Détaillée de l'Endpoint de Prévisions (Open-Meteo)

Ce document détaille l'utilisation de l'endpoint principal de prévisions météorologiques (`/v1/forecast`), en se concentrant sur les paramètres, la structure de réponse et les contraintes.

## 1. 📖 Description de l'Endpoint

| Caractéristique | Détail |
| :--- | :--- |
| **Endpoint** | `https://api.open-meteo.com/v1/forecast` |
| **Fonction** | Fournit des données de prévisions météorologiques (horaires, quotidiennes ou actuelles) pour une paire de coordonnées géographiques spécifiée. |
| **Méthode HTTP** | `GET` |
| **Objectif** | Récupération de données. |

---

## 2. 🧩 Paramètres de la Requête (Query Parameters)

Les paramètres sont ajoutés après le `?` dans l'URL et sont séparés par des `&`.

| Paramètre | Obligatoire | Type | Description |
| :--- | :--- | :--- | :--- |
| **`latitude`** | Oui | Flottant | Coordonnée Nord/Sud du lieu de la prévision. |
| **`longitude`** | Oui | Flottant | Coordonnée Est/Ouest du lieu de la prévision. |
| **`hourly`** | Non | Chaîne de caractères | Liste des variables horaires souhaitées (séparées par des virgules). **Ex :** `temperature_2m, precipitation, pressure_msl`. |
| **`current`** | Non | Chaîne de caractères | Liste des variables des conditions actuelles (instantanées). |
| **`models`** | Non | Chaîne de caractères | Modèles météorologiques à utiliser (ex : `meteofrance_seamless`). |
| **`timezone`** | Non | Chaîne de caractères | Fuseau horaire de la réponse (ex : `auto` ou `Europe/Paris`). |

### Détail des Variables Horaires (`&hourly=...`)

* La plupart des variables sont des **valeurs instantanées** pour l'heure indiquée.
* Certaines variables (comme `precipitation`) sont calculées comme une **somme ou une moyenne** sur l'heure **précédente**.

#### Variables de Pression :

| Variable | Description |
| :--- | :--- |
| **`pressure_msl`** | Pression atmosphérique réduite au niveau moyen de la mer (msl). C'est la pression typiquement utilisée en météorologie. |
| **Pression de Surface** | La pression au niveau de la surface diminue naturellement avec l'altitude, contrairement à `pressure_msl` qui est corrigée. |

---

## 3. 📄 Structure de la Réponse

En cas de succès, l'API renvoie un objet **JSON** (HTTP Status Code `200 OK`).

| Clé JSON | Type | Description |
| :--- | :--- | :--- |
| **`latitude`**, **`longitude`** | Flottant | Coordonnées utilisées pour la prévision. |
| **`timezone`** | Chaîne | Fuseau horaire de la réponse. |
| **`hourly_units`** | Objet | Dictionnaire spécifiant l'unité de mesure pour chaque variable horaire (ex: `"temperature_2m": "°C"`). |
| **`hourly`** | Objet | **Conteneur des données de prévisions.** |
| **`hourly.time`** | Tableau | Liste des horodatages (format ISO8601) pour chaque point de donnée. |
| **`hourly.<variable>`** | Tableau | Liste des valeurs numériques (température, pression, vent, etc.) correspondant à la liste `hourly.time`. |

---

## 4. 🛑 Erreurs Possibles

Les erreurs sont généralement signalées par un code d'état HTTP `400` accompagné d'un message d'erreur explicite dans le corps JSON.

| Code HTTP | Cause la Plus Fréquente | Message JSON Typique |
| :--- | :--- | :--- |
| **400 Bad Request** | **Paramètre Invalide** (ex : Latitude/Longitude en dehors des limites, nom de variable mal orthographié ou non pris en charge). | `{"error": true, "reason": "Invalid parameter '...' "}` |
| **404 Not Found** | URL de base mal orthographiée ou endpoint non existant. | |
| **5xx Server Error** | Problème technique temporaire côté serveur Open-Meteo. | |

---

## 5. ⏳ Limites (Constraints)

L'API Open-Meteo est gratuite, mais elle impose des limites d'utilisation.

| Limite | Détail |
| :--- | :--- |
| **Débit (Rate Limit)** | Limité à un faible nombre de requêtes par jour et par adresse IP (quelques milliers). |
| **Commercialisation**| L'API est réservée à un usage personnel et non commercial. |
| **Période de Prévision** | La durée des prévisions dépend du modèle, mais est généralement limitée à 7, 14 ou 16 jours. |


---

# 🌊 Schéma de Flux d'Intégration pour la Détection de Cyclone

Ce schéma représente le cycle de vie d'une requête, de la planification à la prise de décision.Extrait de codegraph TD
```graph TD
    A[Démarrer: Planification du Cycle d'Alerte] --> B(Préparer Requête GET);

    B --> C{Requête API Open-Meteo};

    C --> |Coordonnées & Modèle Météo-France| D[Endpoint: /v1/forecast];

    D --> E{Serveur API: Traitement des données};

    E --> |Réponse OK (200)| F(Recevoir et Analyser le JSON);
    E --> |Erreur (4xx/5xx)| G[Fin du Processus: Erreur à Journaliser];

    F --> H{Extraire: surface_pressure, wind_gusts_10m, CAPE};

    H --> I{surface_pressure < 1000 hPa ET/OU wind_gusts_10m > 63 km/h?};

    I -- Oui --> J[Alerte Forte: Détection de Système Cyclonique];
    I -- Non --> K[Alerte Faible/Normale: Surveillance Continue];

    J --> L[Notifier l'Utilisateur ou le Système d'Alerte];
    K --> A;
    L --> A;
    G --> A;
```

    style J fill:#f9f,stroke:#333,stroke-width:2px
    style I fill:#ccf,stroke:#333

## 📝 Explication du Schéma de Flux

| **ID** | **Description** | **Type d'Action** / **Forme** |
|----|-------------|------------------------|
| A | **Démarrer**: Le processus s'exécute à intervalles réguliers (ex: toutes les 6 heures) pour une surveillance continue. | Début/Fin du Cycle |
| B | **Préparer Requête GET**: Construction de l'URL avec les paramètres critiques (hourly=..., models=meteofrance_seamless). | Processus (Rectangle) |
| C | **Requête API Open-Meteo**: Envoi de la requête HTTP vers le serveur. | Processus (Rectangle arrondi) |
| D | **Endpoint: Cible de la requête** : /v1/forecast. | Processus (Rectangle) |
| E | **Serveur API**: Traitement des données: Le serveur exécute le modèle Météo-France et prépare la réponse. | Processus (Rectangle arrondi) |
| F | **Recevoir et Analyser le JSON**: Réception de la réponse (statut 200 OK) et vérification de la structure du corps JSON. | Processus (Rectangle) |
| G | **Fin du Processus**: Erreur à Journaliser: En cas d'échec (timeout, 400, 500), l'erreur est enregistrée, et le cycle redémarre (retour à A). | Fin/Arrêt (Rectangle) |
| H | **Extraire les Données**: Récupération des valeurs clés (surface_pressure, wind_gusts_10m, CAPE) à partir des tableaux horaires. | Processus (Rectangle) |
| I | **Décision d'Alerte**: Le cœur de la logique. Vérification si les seuils critiques sont atteints pour le vent et/ou la pression (seuil Tempête Tropicale ici). | Décision (Losange) |
| J | **Alerte Forte**: Les seuils sont franchis. Action immédiate requise. | Processus (Rectangle) |
| K | **Alerte Faible/Normale**: Les conditions sont stables. Le système retourne en mode surveillance. | Processus (Rectangle) |
| L | **Notifier**: Envoi d'une notification ou déclenchement d'une alarme dans le système d'alerte. | Processus (Rectangle) |
