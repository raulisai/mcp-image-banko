import asyncio
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from api.wikimedia_client import WikimediaClient
from api.sourcesplash_client import SourceSplashClient

async def test_clients():
    print("Testing Wikimedia Client...")
    wiki = WikimediaClient()
    try:
        res = await wiki.search("cat", limit=1)
        print("Wikimedia Result:", res)
    except Exception as e:
        print(f"Wikimedia Error: {e}")

    print("\nTesting SourceSplash Client...")
    splash = SourceSplashClient()
    try:
        res = await splash.search("dog", limit=1)
        print("SourceSplash Result:", res)
    except Exception as e:
        print(f"SourceSplash Error: {e}")

    print("\nTesting Pexels Client...")
    from api.pexels_client import PexelsClient
    pexels = PexelsClient()
    try:
        res = await pexels.search("nature", limit=1)
        # Setup specific print to avoid dumping huge JSON
        if "error" in res:
             print("Pexels Result:", res)
        else:
             print(f"Pexels Result Success: Found {len(res.get('photos', []))} photos.")
             if res.get('photos'):
                 print(f"First photo: {res['photos'][0]['url']}")
    except Exception as e:
        print(f"Pexels Error: {e}")

    print("\nTesting Unsplash Client...")
    from api.unsplash_client import UnsplashClient
    unsplash = UnsplashClient()
    try:
        res = await unsplash.search("city", limit=1)
        if "error" in res:
            print("Unsplash Result:", res)
        else:
            print(f"Unsplash Result Success: Found {len(res.get('results', []))} results.")
            if res.get('results'):
                print(f"First photo: {res['results'][0]['urls']['regular']}")
    except Exception as e:
        print(f"Unsplash Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_clients())
