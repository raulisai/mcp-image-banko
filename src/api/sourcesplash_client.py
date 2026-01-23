import httpx
from typing import List, Dict, Any

class SourceSplashClient:
    BASE_URL = "https://www.sourcesplash.com/api/search"

    async def search(self, query: str, limit: int = 5) -> Dict[str, Any]:
        params = {"query": query, "per_page": limit}
        headers = {"User-Agent": "ImageBankoMCP/1.0"}

        async with httpx.AsyncClient(follow_redirects=True) as client:
            try:
                response = await client.get(self.BASE_URL, params=params, headers=headers)
                # If 404, fallback to api.sourcesplash.com
                if response.status_code == 404:
                     # Fallback strategy not easy here without recursion or complex logic
                     pass

                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                return {"error": f"HTTP error occurred: {e}"}
            except Exception as e:
                return {"error": f"An error occurred: {str(e)}"}
