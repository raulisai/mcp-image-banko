from mcp.server.fastmcp import FastMCP
import httpx
import os
from dotenv import load_dotenv
from api.pexels_client import PexelsClient
from api.unsplash_client import UnsplashClient
from api.wikimedia_client import WikimediaClient
from api.sourcesplash_client import SourceSplashClient

# Load environment variables
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("image-banko")

# Initialize Clients
pexels_client = PexelsClient()
unsplash_client = UnsplashClient()
wikimedia_client = WikimediaClient()
sourcesplash_client = SourceSplashClient()

@mcp.tool()
async def search_free_images(query: str, limit: int = 5) -> str:
    """
    Search for free/CC0 images using Wikimedia Commons (FreeImageDomain).
    No API Key required.
    """
    results = await wikimedia_client.search(query, limit)
    return str(results)

@mcp.tool()
async def search_pexels(query: str, limit: int = 5) -> str:
    """
    Search for images on Pexels. Requires PEXELS_API_KEY env var.
    """
    results = await pexels_client.search(query, limit)
    return str(results)

@mcp.tool()
async def search_unsplash(query: str, limit: int = 5) -> str:
    """
    Search for images on Unsplash. Requires UNSPLASH_ACCESS_KEY env var.
    """
    results = await unsplash_client.search(query, limit)
    return str(results)

@mcp.tool()
async def search_sourcesplash(query: str, limit: int = 5) -> str:
    """
    Search for images via SourceSplash. Free (rate limited).
    """
    results = await sourcesplash_client.search(query, limit)
    return str(results)

if __name__ == "__main__":
    mcp.run()
