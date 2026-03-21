from fastmcp import FastMCP

from coda_mcp.client import coda_client
from coda_mcp.dependencies import CodaApiKeyDependency
from coda_mcp.models import (
    ColumnListItem,
    ControlDetail,
    ControlListItem,
    FormulaDetail,
    FormulaListItem,
    MutationStatusResponse,
    ResolveBrowserLinkQuery,
    ResolveBrowserLinkResponse,
    TableListItem,
    WhoamiResponse,
)
from coda_mcp.models.workspaces import WorkspaceItem, WorkspacesListResponse


def register(mcp: FastMCP) -> None:
    @mcp.tool()
    async def whoami(coda_api_key: str = CodaApiKeyDependency) -> WhoamiResponse:
        """Return details about the Coda account associated with the current API key."""
        return await coda_client.miscellaneous.get_whoami(api_key=coda_api_key)

    @mcp.tool()
    async def resolve_link(
        url: str, coda_api_key: str = CodaApiKeyDependency
    ) -> ResolveBrowserLinkResponse:
        """Resolve a Coda browser URL into its resource type and ID. Use this when the user pastes any Coda link — it works for docs, pages, tables, and rows."""
        return await coda_client.miscellaneous.get_resolve_browser_link(
            ResolveBrowserLinkQuery.model_validate({"url": url}),
            api_key=coda_api_key,
        )

    @mcp.tool()
    async def list_tables(
        doc_id: str, coda_api_key: str = CodaApiKeyDependency
    ) -> list[TableListItem]:
        """List all tables and views in a Coda doc. Always call this before list_rows or upsert_row to get correct table IDs."""
        data = await coda_client.tables.list_tables(doc_id, api_key=coda_api_key)
        return data.items

    @mcp.tool()
    async def list_columns(
        doc_id: str, table_id: str, coda_api_key: str = CodaApiKeyDependency
    ) -> list[ColumnListItem]:
        """List all columns in a Coda table. Call this before upsert_row to find the correct column IDs or names to use in cells."""
        data = await coda_client.tables.list_columns(doc_id, table_id, api_key=coda_api_key)
        return data.items

    @mcp.tool()
    async def get_mutation_status(
        request_id: str, coda_api_key: str = CodaApiKeyDependency
    ) -> MutationStatusResponse:
        """Check whether a queued Coda mutation (row upsert, delete, page update) has completed. Pass the request_id from the queued response."""
        return await coda_client.miscellaneous.get_mutation_status(request_id, api_key=coda_api_key)

    @mcp.tool()
    async def list_workspaces(coda_api_key: str = CodaApiKeyDependency) -> WorkspacesListResponse:
        """List all Coda workspaces accessible with the current API key."""
        return await coda_client.workspaces.list_workspaces(api_key=coda_api_key)

    @mcp.tool()
    async def get_workspace(
        workspace_id: str, coda_api_key: str = CodaApiKeyDependency
    ) -> WorkspaceItem:
        """Get details for a specific Coda workspace."""
        return await coda_client.workspaces.get_workspace(workspace_id, api_key=coda_api_key)

    @mcp.tool()
    async def list_formulas(
        doc_id: str, coda_api_key: str = CodaApiKeyDependency
    ) -> list[FormulaListItem]:
        """List all named formulas in a Coda doc."""
        data = await coda_client.formulas_controls.get_formulas_list(doc_id, api_key=coda_api_key)
        return data.items

    @mcp.tool()
    async def get_formula(
        doc_id: str, formula_id_or_name: str, coda_api_key: str = CodaApiKeyDependency
    ) -> FormulaDetail:
        """Get the value and details of a named formula in a Coda doc."""
        return await coda_client.formulas_controls.get_formula(
            doc_id, formula_id_or_name, api_key=coda_api_key
        )

    @mcp.tool()
    async def list_controls(
        doc_id: str, coda_api_key: str = CodaApiKeyDependency
    ) -> list[ControlListItem]:
        """List all controls (sliders, dropdowns, etc.) in a Coda doc."""
        data = await coda_client.formulas_controls.get_controls_list(doc_id, api_key=coda_api_key)
        return data.items

    @mcp.tool()
    async def get_control(
        doc_id: str, control_id_or_name: str, coda_api_key: str = CodaApiKeyDependency
    ) -> ControlDetail:
        """Get the current value and details of a control in a Coda doc."""
        return await coda_client.formulas_controls.get_control(
            doc_id, control_id_or_name, api_key=coda_api_key
        )
