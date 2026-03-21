from fastmcp import FastMCP
from coda_mcp.client import coda_get
from coda_mcp.models import CodaDoc


def register(mcp: FastMCP) -> None:

    @mcp.tool()
    async def list_docs(query: str = "") -> list[CodaDoc]:
        """List all Coda docs accessible with your API key. Optionally filter by name."""
        params = {}
        if query:
            params["query"] = query
        data = await coda_get("/docs", params=params)
        return [CodaDoc.model_validate(item) for item in data["items"]]

    @mcp.tool()
    async def search_docs(query: str) -> list[CodaDoc]:
        """Search for Coda docs by name or keyword."""
        data = await coda_get("/docs", params={"query": query})
        return [CodaDoc.model_validate(item) for item in data["items"]]
