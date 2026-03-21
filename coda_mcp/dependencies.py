"""Coda API auth for MCP tools — use ``CodaApiKeyDependency`` on each tool."""

from fastmcp.dependencies import Depends
from fastmcp.exceptions import ToolError
from fastmcp.server.dependencies import get_http_headers

from coda_mcp.config import settings

__all__ = ["CodaApiKeyDependency", "Depends", "get_coda_api_key"]


def get_coda_api_key() -> str:
    """Resolve the Coda API key: MCP ``Authorization: Bearer``, else ``CODA_API_KEY``."""
    headers = get_http_headers(include={"authorization"})
    auth = headers.get("authorization", "")
    token = auth.removeprefix("Bearer ").strip()

    if token:
        return token

    if settings.coda_api_key is not None:
        return settings.coda_api_key.get_secret_value()

    raise ToolError(
        "No Coda API key found. Set CODA_API_KEY (local) or send Authorization: Bearer <key> on the MCP request (cloud)."
    )


# Shared ``Depends`` instance — use as: ``coda_api_key: str = CodaApiKeyDependency``
CodaApiKeyDependency = Depends(get_coda_api_key)
