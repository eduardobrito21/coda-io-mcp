from functools import cached_property

import httpx

from coda_mcp.config import settings

from .automations import AutomationsClient
from .common import CodaRequestMixin
from .doc_structure import DocStructureClient
from .docs import DocsClient
from .folders import FoldersClient
from .formulas_controls import FormulasControlsClient
from .miscellaneous import MiscellaneousClient
from .tables import TablesClient
from .workspaces import WorkspacesClient


class CodaClient(CodaRequestMixin):
    """Async HTTP client for the Coda REST API (v1), grouped by API doc sections."""

    def __init__(self):
        self.http = httpx.AsyncClient(timeout=httpx.Timeout(30.0))
        self.base_url = f"{settings.coda_base_url.rstrip('/')}/"

    @cached_property
    def docs(self) -> DocsClient:
        return DocsClient(http=self.http, base_url=self.base_url)

    @cached_property
    def doc_structure(self) -> DocStructureClient:
        return DocStructureClient(http=self.http, base_url=self.base_url)

    @cached_property
    def folders(self) -> FoldersClient:
        return FoldersClient(http=self.http, base_url=self.base_url)

    @cached_property
    def tables(self) -> TablesClient:
        return TablesClient(http=self.http, base_url=self.base_url)

    @cached_property
    def formulas_controls(self) -> FormulasControlsClient:
        return FormulasControlsClient(http=self.http, base_url=self.base_url)

    @cached_property
    def miscellaneous(self) -> MiscellaneousClient:
        return MiscellaneousClient(http=self.http, base_url=self.base_url)

    @cached_property
    def automations(self) -> AutomationsClient:
        return AutomationsClient(http=self.http, base_url=self.base_url)

    @cached_property
    def workspaces(self) -> WorkspacesClient:
        return WorkspacesClient(http=self.http, base_url=self.base_url)

    async def aclose(self) -> None:
        await self.http.aclose()


coda_client = CodaClient()
