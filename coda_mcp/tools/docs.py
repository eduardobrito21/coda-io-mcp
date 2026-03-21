from fastmcp import FastMCP

from coda_mcp.client import coda_client
from coda_mcp.dependencies import CodaApiKeyDependency
from coda_mcp.models import CodaDoc, DocsListQuery


def register(mcp: FastMCP) -> None:

    @mcp.tool()
    async def list_docs(query: str = "", coda_api_key: str = CodaApiKeyDependency) -> list[CodaDoc]:
        """List all Coda docs accessible with your API key. Optionally filter by name."""
        params = DocsListQuery.model_validate({"query": query}) if query else None
        data = await coda_client.docs.list_docs(params, api_key=coda_api_key)
        return [
            CodaDoc.model_validate(
                {
                    "id": item.id,
                    "name": item.name,
                    "browserLink": str(item.browser_link),
                },
            )
            for item in data.items
        ]

    @mcp.tool()
    async def search_docs(query: str, coda_api_key: str = CodaApiKeyDependency) -> list[CodaDoc]:
        """Search for Coda docs by name or keyword."""
        data = await coda_client.docs.list_docs(
            DocsListQuery.model_validate({"query": query}),
            api_key=coda_api_key,
        )
        return [
            CodaDoc.model_validate(
                {
                    "id": item.id,
                    "name": item.name,
                    "browserLink": str(item.browser_link),
                },
            )
            for item in data.items
        ]
