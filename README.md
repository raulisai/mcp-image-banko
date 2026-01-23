# Image Banko MCP Server

A Custom MCP Server that provides tools to search for images from multiple sources.

## Supported APIs

1.  **FreeImageDomain** (via Wikimedia Commons) - No key required.
2.  **Pexels** - Requires `PEXELS_API_KEY`.
3.  **Unsplash** - Requires `UNSPLASH_ACCESS_KEY`.
4.  **SourceSplash** - Free use (Experimental/Beta).

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configuration**:
    Create a `.env` file based on `.env.example` and add your API keys.

    ```env
    PEXELS_API_KEY=your_key
    UNSPLASH_ACCESS_KEY=your_key
    ```

## Usage

### Running the Server

Run the server using `mcp` (if installed globally) or python:

```bash
# Using fastmcp dev server
mcp dev src/server.py
```

Or configure it in your MCP client (e.g., Claude Desktop, Antigravity) to run:

```json
{
  "mcpServers": {
    "image-banko": {
      "command": "python",
      "args": ["/path/to/mcp-image-banko/src/server.py"],
      "env": {
        "PEXELS_API_KEY": "...",
        "UNSPLASH_ACCESS_KEY": "..."
      }
    }
  }
}
```

### Tools

- `search_free_images(query, limit)`: Search Wikimedia Commons.
- `search_pexels(query, limit)`: Search Pexels.
- `search_unsplash(query, limit)`: Search Unsplash.
- `search_sourcesplash(query, limit)`: Search SourceSplash.
