# ================================================================
# config.py — Configuration globale du serveur MCP Paperform
# ================================================================
# Ce fichier centralise toutes les variables de configuration.
# Chaque outil l'importe pour accéder à la clé API et aux headers.
# ================================================================

import os

# URL de base de l'API Paperform — ne change jamais
PAPERFORM_BASE_URL = "https://api.paperform.co/v1"

# Clé API Paperform — lue depuis les variables d'environnement (Railway)
# Ne jamais écrire la vraie clé ici directement !
PAPERFORM_API_KEY = os.environ.get("PAPERFORM_API_KEY", "")

# Port d'écoute du serveur — Railway injecte automatiquement PORT
PORT = int(os.environ.get("PORT", 8000))


def get_auth_headers() -> dict:
    """
    Retourne les headers HTTP d'authentification pour l'API Paperform.
    Cette fonction est importée et appelée dans chaque fichier d'outil.
    """
    return {
        "Authorization": f"Bearer {PAPERFORM_API_KEY}",
        "Accept": "application/json"
    }