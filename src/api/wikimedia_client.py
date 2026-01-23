import httpx
from typing import List, Dict, Any

class WikimediaClient:
    BASE_URL = "https://commons.wikimedia.org/w/api.php"

    async def search(self, query: str, limit: int = 5) -> Dict[str, Any]:
        # Search for images in Wikimedia Commons
        # Wikimedia requires a descriptive User-Agent
        headers = {
            "User-Agent": "ImageBankoMCP/1.0 (raul@example.com) based on mcp-image-banko"
        }
        params = {
            "action": "query",
            "format": "json",
            "generator": "search",
            "gsrnamespace": 6,  # File namespace
            "gsrsearch": f"filetype:bitmap|drawing {query}",
            "gsrlimit": limit,
            "prop": "imageinfo",
            "iiprop": "url|mime|size",
        }

        async with httpx.AsyncClient(follow_redirects=True) as client:
            try:
                response = await client.get(self.BASE_URL, params=params, headers=headers)
                response.raise_for_status()
                data = response.json()
                
                # Normalize output to be friendlier
                results = []
                pages = data.get("query", {}).get("pages", {})
                for page_id, page_data in pages.items():
                    if "imageinfo" in page_data:
                        info = page_data["imageinfo"][0]
                        results.append({
                            "title": page_data.get("title", "").replace("File:", ""),
                            "url": info.get("url"),
                            "thumbnail": info.get("thumburl"), # Wikimedia API usually requires iiurlwidth for thumb, assume full url for now or handle complexity
                            "width": info.get("width"),
                            "height": info.get("height"),
                            "source": "Wikimedia Commons"
                        })
                
                return {"results": results}

            except httpx.HTTPStatusError as e:
                return {"error": f"HTTP error occurred: {e}"}
            except Exception as e:
                return {"error": f"An error occurred: {str(e)}"}
