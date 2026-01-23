import httpx
import os
from typing import List, Dict, Any

class PexelsClient:
    BASE_URL = "https://api.pexels.com/v1"

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("PEXELS_API_KEY")

    async def search(self, query: str, limit: int = 5) -> Dict[str, Any]:
        if not self.api_key:
            return {"error": "PEXELS_API_KEY is missing"}
        
        headers = {"Authorization": self.api_key}
        params = {"query": query, "per_page": limit}

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.BASE_URL}/search", headers=headers, params=params)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                return {"error": f"HTTP error occurred: {e}", "details": e.response.text}
            except Exception as e:
                return {"error": f"An error occurred: {str(e)}"}
