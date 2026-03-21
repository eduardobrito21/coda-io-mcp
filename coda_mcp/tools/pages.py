from fastmcp import FastMCP
from coda_mcp.client import coda_get, coda_put
from coda_mcp.models import CodaPage


def register(mcp: FastMCP) -> None:

    @mcp.tool()
    async def list_pages(doc_id: str) -> list[CodaPage]:
        """List all pages in a Coda doc."""
        data = await coda_get(f"/docs/{doc_id}/pages")
        return [CodaPage.model_validate(item) for item in data["items"]]

    @mcp.tool()
    async def get_page(doc_id: str, page_id: str) -> str:
        """Get the content of a Coda page as markdown."""
        data = await coda_get(
            f"/docs/{doc_id}/pages/{page_id}/export",
            params={"outputFormat": "markdown"},
        )
        return data["markdown"]

    @mcp.tool()
    async def update_page(doc_id: str, page_id: str, content: str) -> str:
        """Replace the full content of a Coda page."""
        await coda_put(f"/docs/{doc_id}/pages/{page_id}", body={"content": content})
        return "Page updated successfully."
