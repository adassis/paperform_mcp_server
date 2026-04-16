# ================================================================
# tools/get_form.py — Outil MCP : Obtenir un formulaire spécifique
# Endpoint Paperform : GET /forms/{slug_or_id}
# ================================================================

import httpx
from config import PAPERFORM_BASE_URL, get_auth_headers


def get_form(slug_or_id: str) -> dict:
    """
    Retourne les détails complets d'un formulaire identifié
    par son slug ou son ID unique.

    ℹ️ Le slug est la partie de l'URL avant '.paperform.co'.
    Ex : pour 'https://newsletter.paperform.co', le slug est 'newsletter'.

    Args:
        slug_or_id: Le slug, le slug personnalisé, ou l'ID du formulaire

    Returns:
        Un dictionnaire JSON contenant les détails du formulaire.
    """
    with httpx.Client() as client:
        response = client.get(
            # L'identifiant est inséré directement dans l'URL
            f"{PAPERFORM_BASE_URL}/forms/{slug_or_id}",
            headers=get_auth_headers()
        )
        response.raise_for_status()
        return response.json()