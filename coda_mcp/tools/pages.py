from fastmcp import FastMCP

from coda_mcp.client import coda_client
from coda_mcp.dependencies import CodaApiKeyDependency
from coda_mcp.models import CodaPage, PutPageBody


def register(mcp: FastMCP) -> None:

    @mcp.tool()
    async def list_pages(doc_id: str, coda_api_key: str = CodaApiKeyDependency) -> list[CodaPage]:
        """List all pages in a Coda doc."""
        data = await coda_client.doc_structure.get_pages_list(doc_id, api_key=coda_api_key)
        return [CodaPage(id=item.id, name=item.name) for item in data.items]

    @mcp.tool()
    async def get_page(doc_id: str, page_id: str, coda_api_key: str = CodaApiKeyDependency) -> str:
        """Get the content of a Coda page as markdown (async export + download)."""
        return await coda_client.doc_structure.export_page_markdown(
            doc_id, page_id, api_key=coda_api_key
        )

    @mcp.tool()
    async def update_page(
        doc_id: str, page_id: str, content: str, coda_api_key: str = CodaApiKeyDependency
    ) -> str:
        """Replace the full content of a Coda page."""
        body = PutPageBody.model_validate(
            {
                "contentUpdate": {
                    "insertionMode": "replace",
                    "canvasContent": {"format": "markdown", "content": content},
                },
            },
        )
        result = await coda_client.doc_structure.put_page(
            doc_id, page_id, body, api_key=coda_api_key
        )
        return f"Page update queued (request_id={result.request_id}, page_id={result.id})."
