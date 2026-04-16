# ================================================================
# main.py — Point d'entrée du serveur MCP Paperform
# ================================================================
# Ce fichier est le seul qu'on lance directement.
# Il importe les outils depuis le dossier tools/ et les enregistre
# auprès du serveur MCP FastMCP.
# ================================================================

from mcp.server.fastmcp import FastMCP

# Import de la configuration (port de démarrage)
from config import PORT

# Import de tous les outils depuis le dossier tools/
# Grâce au __init__.py, on peut tout importer en une ligne
from tools import (
    list_forms,
    get_form,
    list_form_fields,
    list_form_submissions
)


# ================================================================
# INITIALISATION DU SERVEUR MCP
# ================================================================

mcp = FastMCP(
    name="Paperform MCP Server",
    description="Serveur MCP pour interagir avec l'API Paperform. Permet de lister les formulaires, leurs champs et leurs soumissions."
)


# ================================================================
# ENREGISTREMENT DES OUTILS
# ================================================================
# Le décorateur @mcp.tool() enregistre chaque fonction comme un
# outil MCP disponible pour les agents Dust.
# ================================================================

mcp.tool()(list_forms)
mcp.tool()(get_form)
mcp.tool()(list_form_fields)
mcp.tool()(list_form_submissions)


# ================================================================
# DÉMARRAGE DU SERVEUR
# ================================================================

if __name__ == "__main__":
    print(f"🚀 Démarrage du serveur MCP Paperform sur le port {PORT}...")
    mcp.run(
        transport="streamable-http",  # Compatible Dust
        host="0.0.0.0",               # Écoute sur toutes les interfaces (requis pour Railway)
        port=PORT
    )