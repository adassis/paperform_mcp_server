# ================================================================
# tools/get_submission.py — Outil MCP : Obtenir une soumission
# Endpoint Paperform : GET /submissions/{id}
# ================================================================

import httpx
from config import PAPERFORM_BASE_URL, get_auth_headers


def get_submission(submission_id: str) -> dict:
    """
    Retourne les données complètes d'une soumission spécifique
    identifiée par son ID unique.

    Contient toutes les réponses aux champs du formulaire,
    les métadonnées (date, IP, etc.) et les informations du soumetteur.

    Args:
        submission_id: L'ID unique de la soumission

    Returns:
        Un dictionnaire JSON contenant toutes les données de la soumission.
    """
    with httpx.Client() as client:
        response = client.get(
            f"{PAPERFORM_BASE_URL}/submissions/{submission_id}",
            headers=get_auth_headers()
        )
        response.raise_for_status()
        return response.json()