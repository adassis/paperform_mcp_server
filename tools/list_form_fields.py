# ================================================================
# tools/list_form_fields.py — Outil MCP : Lister les champs d'un formulaire
# Endpoint Paperform : GET /forms/{slug_or_id}/fields
# ================================================================

import httpx
from config import PAPERFORM_BASE_URL, get_auth_headers


def list_form_fields(
    slug_or_id: str,
    search: str = ""
) -> dict:
    """
    Retourne la liste de tous les champs (questions) d'un formulaire.

    Les types de champs incluent : texte libre, choix multiples,
    dropdown, calcul, produits, échelle, etc.

    Args:
        slug_or_id: Le slug, le slug personnalisé, ou l'ID du formulaire
        search: Rechercher des champs par nom (optionnel)

    Returns:
        Un dictionnaire JSON contenant la liste des champs du formulaire.
    """
    # Le paramètre search est optionnel
    params = {}
    if search:
        params["search"] = search

    with httpx.Client() as client:
        response = client.get(
            # URL imbriquée : /forms/{id}/fields
            f"{PAPERFORM_BASE_URL}/forms/{slug_or_id}/fields",
            headers=get_auth_headers(),
            params=params
        )
        response.raise_for_status()
        return response.json()