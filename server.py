import uvicorn
from mcp.server.fastmcp import FastMCP
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from config import PORT, MCP_BEARER_TOKEN
from tools import (
    list_forms,
    get_form,
    list_form_fields,
    list_form_submissions
)

# ── Initialisation ─────────────────────────────────────────────
mcp = FastMCP(
    name="paperform-server",
    host="0.0.0.0",
    port=PORT
)

# ── Enregistrement des outils ──────────────────────────────────
mcp.tool()(list_forms)
mcp.tool()(get_form)
mcp.tool()(list_form_fields)
mcp.tool()(list_form_submissions)

# ── Middleware d'authentification ──────────────────────────────
class BearerAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if MCP_BEARER_TOKEN:
            auth = request.headers.get("Authorization", "")
            if not auth.startswith("Bearer ") or auth[7:].strip() != MCP_BEARER_TOKEN:
                return JSONResponse({"error": "Non autorisé"}, status_code=401)
        return await call_next(request)

# ── Démarrage ──────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"🚀 Serveur MCP Paperform démarré sur le port {PORT}")
    print(f"🔐 Auth : {'Activée' if MCP_BEARER_TOKEN else 'DÉSACTIVÉE'}")

    app = mcp.streamable_http_app()
    app.add_middleware(BearerAuthMiddleware)
    uvicorn.run(app, host="0.0.0.0", port=PORT)