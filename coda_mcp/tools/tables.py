from fastmcp import FastMCP
from coda_mcp.client import coda_get, coda_post, coda_delete
from coda_mcp.models import CodaCell, CodaRow


def register(mcp: FastMCP) -> None:

    @mcp.tool()
    async def list_rows(
        doc_id: str,
        table_id: str,
        limit: int = 25,
        query: str = "",
    ) -> list[CodaRow]:
        """List rows from a Coda table. Optionally filter with a query string."""
        params: dict = {"limit": limit, "valueFormat": "simpleWithArrays"}
        if query:
            params["query"] = query
        data = await coda_get(f"/docs/{doc_id}/tables/{table_id}/rows", params=params)
        return [CodaRow.model_validate(item) for item in data["items"]]

    @mcp.tool()
    async def upsert_row(
        doc_id: str,
        table_id: str,
        cells: list[CodaCell],
        key_columns: list[str] = [],
    ) -> dict:
        """Insert or update a row in a Coda table. Provide key_columns to upsert instead of always inserting."""
        body = {
            "rows": [{"cells": [c.model_dump() for c in cells]}],
            "keyColumns": key_columns,
        }
        return await coda_post(f"/docs/{doc_id}/tables/{table_id}/rows", body=body)

    @mcp.tool()
    async def delete_row(doc_id: str, table_id: str, row_id: str) -> dict:
        """Delete a row from a Coda table by row ID."""
        return await coda_delete(f"/docs/{doc_id}/tables/{table_id}/rows/{row_id}")
