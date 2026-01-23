import httpx
import os
from typing import List, Dict, Any

class UnsplashClient:
    BASE_URL = "https://api.unsplash.com"

    def __init__(self, access_key: str = None):
        self.access_key = access_key or os.getenv("UNSPLASH_ACCESS_KEY")

    async def search(self, query: str, limit: int = 5) -> Dict[str, Any]:
        if not self.access_key:
            return {"error": "UNSPLASH_ACCESS_KEY is missing"}
        
        headers = {"Authorization": f"Client-ID {self.access_key}"}
        params = {"query": query, "per_page": limit}

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.BASE_URL}/search/photos", headers=headers, params=params)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                return {"error": f"HTTP error occurred: {e}", "details": e.response.text}
            except Exception as e:
                return {"error": f"An error occurred: {str(e)}"}
