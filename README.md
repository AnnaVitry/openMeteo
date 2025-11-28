```
project_openmeteo/
├── .env                  # Configuration (Clés API, URL de base)
├── main.py               # Point d'entrée de l'application
├── services/             # Fonctions d'appel API spécifiques
│   └── weather_api.py
├── config/               # Gestion des variables d'environnement
│   └── settings.py
└── utils/                # Fonctions utilitaires (Gestion des erreurs)
    └── error_handler.py
```