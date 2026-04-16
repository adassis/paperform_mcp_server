# ================================================================
# tools/list_forms.py — Outil MCP : Lister les formulaires
# Endpoint Paperform : GET /forms
# ================================================================

import httpx
# On importe la config depuis le fichier config.py (dossier parent)
from config import PAPERFORM_BASE_URL, get_auth_headers


def list_forms(
    search: str = "",
    limit: int = 20,
    skip: int = 0,
    sort: str = "DESC"
) -> dict:
    """
    Retourne la liste de tous les formulaires accessibles
    par l'utilisateur authentifié sur Paperform.

    Args:
        search: Rechercher des formulaires par titre (optionnel)
        limit: Nombre de résultats à retourner (max 100, défaut 20)
        skip: Nombre de résultats à ignorer pour la pagination (défaut 0)
        sort: Direction du tri - 'ASC' ou 'DESC' (défaut 'DESC')

    Returns:
        Un dictionnaire JSON contenant la liste des formulaires.
    """
    # Construction des paramètres de la requête
    params = {
        "limit": limit,
        "skip": skip,
        "sort": sort
    }
    # On n'ajoute 'search' que s'il est renseigné
    if search:
        params["search"] = search

    with httpx.Client() as client:
        response = client.get(
            f"{PAPERFORM_BASE_URL}/forms",
            headers=get_auth_headers(),
            params=params
        )
        # Lève une exception si le serveur retourne une erreur HTTP
        response.raise_for_status()
        return response.json()