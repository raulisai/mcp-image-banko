import asyncio
import os
from dotenv import load_dotenv
import sys

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from api.wikimedia_client import WikimediaClient
from api.pexels_client import PexelsClient
from api.unsplash_client import UnsplashClient
from api.sourcesplash_client import SourceSplashClient

async def check():
    load_dotenv()
    
    clients = {
        "Wikimedia": WikimediaClient(),
        "Pexels": PexelsClient(),
        "Unsplash": UnsplashClient(),
        "SourceSplash": SourceSplashClient()
    }
    
    for name, client in clients.items():
        try:
            print(f"--- {name} ---")
            res = await client.search("nature", limit=1)
            if "error" in res:
                print(f"Status: ERROR - {res['error']}")
            else:
                print(f"Status: SUCCESS - Found results")
        except Exception as e:
            print(f"Status: EXCEPTION - {str(e)}")

if __name__ == "__main__":
    asyncio.run(check())
