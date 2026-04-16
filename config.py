import os

PAPERFORM_BASE_URL = "https://api.paperform.co/v1"
PAPERFORM_API_KEY = os.environ.get("PAPERFORM_API_KEY", "")
PORT = int(os.environ.get("PORT", 8000))

# Token pour protéger l'accès au serveur MCP lui-même
MCP_BEARER_TOKEN = os.environ.get("MCP_BEARER_TOKEN", "")

def get_auth_headers() -> dict:
    return {
        "Authorization": f"Bearer {PAPERFORM_API_KEY}",
        "Accept": "application/json"
    }