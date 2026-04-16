from mcp.server.fastmcp import FastMCP

from config import PORT

from tools import (
    list_forms,
    get_form,
    list_form_fields,
    list_form_submissions
)

mcp = FastMCP("Paperform MCP Server")

mcp.tool()(list_forms)
mcp.tool()(get_form)
mcp.tool()(list_form_fields)
mcp.tool()(list_form_submissions)

if __name__ == "__main__":
    print(f"🚀 Démarrage du serveur MCP Paperform sur le port {PORT}...")
    mcp.settings.host = "0.0.0.0"
    mcp.settings.port = PORT
    mcp.run(transport="streamable-http")