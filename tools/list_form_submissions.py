# ================================================================
# tools/list_form_submissions.py — Outil MCP : Lister les soumissions
# Endpoint Paperform : GET /forms/{slug_or_id}/submissions
# ================================================================

import httpx
from config import PAPERFORM_BASE_URL, get_auth_headers


def list_form_submissions(
    slug_or_id: str,
    limit: int = 20,
    skip: int = 0,
    sort: str = "DESC",
    after_date: str = "",
    before_date: str = ""
) -> dict:
    """
    Retourne la liste des soumissions (réponses) pour un formulaire.

    Chaque soumission contient les valeurs de TOUS les champs du formulaire,
    ce qui permet d'analyser les réponses par champ.

    Args:
        slug_or_id: Le slug, le slug personnalisé, ou l'ID du formulaire
        limit: Nombre de résultats à retourner (max 100, défaut 20)
        skip: Nombre de résultats à ignorer pour la pagination (défaut 0)
        sort: Direction du tri - 'ASC' ou 'DESC' (défaut 'DESC')
        after_date: Soumissions après cette date UTC, format ISO 8601 (optionnel)
                    Ex : '2024-01-01T00:00:00Z'
        before_date: Soumissions avant cette date UTC, format ISO 8601 (optionnel)

    Returns:
        Un dictionnaire JSON contenant la liste des soumissions.
    """
    params = {
        "limit": limit,
        "skip": skip,
        "sort": sort
    }
    # Les filtres de date sont ajoutés uniquement s'ils sont renseignés
    if after_date:
        params["after_date"] = after_date
    if before_date:
        params["before_date"] = before_date

    with httpx.Client() as client:
        response = client.get(
            # URL imbriquée : /forms/{id}/submissions
            f"{PAPERFORM_BASE_URL}/forms/{slug_or_id}/submissions",
            headers=get_auth_headers(),
            params=params
        )
        response.raise_for_status()
        return response.json()