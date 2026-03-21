import httpx
from coda_mcp.config import settings


def _headers() -> dict:
    return {
        "Authorization": f"Bearer {settings.coda_api_key.get_secret_value()}",
        "Content-Type": "application/json",
    }


async def coda_get(path: str, params: dict = {}) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{settings.coda_base_url}{path}",
            headers=_headers(),
            params=params,
        )
        response.raise_for_status()
        return response.json()


async def coda_post(path: str, body: dict) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.coda_base_url}{path}",
            headers=_headers(),
            json=body,
        )
        response.raise_for_status()
        return response.json()


async def coda_put(path: str, body: dict) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"{settings.coda_base_url}{path}",
            headers=_headers(),
            json=body,
        )
        response.raise_for_status()
        return response.json()


async def coda_delete(path: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            f"{settings.coda_base_url}{path}",
            headers=_headers(),
        )
        response.raise_for_status()
        return response.json()
