from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from figma import get_file, get_node, get_file_from_url, get_node_from_url, set_figma_token

load_dotenv(".env")

# Create an MCP server
mcp = FastMCP(
    name="Figma MCP Server",
    host="0.0.0.0",  # only used for SSE transport (localhost)
    port=8050,  # only used for SSE transport (set this to any port)
)

@mcp.tool()
def getFile(file_key: str) -> any:
    """Fetch the Figma File using File Key"""
    return get_file(file_key)

@mcp.tool()
def getNode(file_key: str, node_id: str) -> any:
    """Fetch the Figma Node using File Key and Node Id"""
    return get_node(file_key, node_id)

@mcp.tool()
def getFileFromUrl(figma_url: str) -> any:
    """Fetch the Figma File using Figma Url"""
    return get_file_from_url(figma_url)

@mcp.tool()
def getNodeFromUrl(figma_url: str) -> any:
    """Fetch the Figma Node using Figma Url"""
    return get_node_from_url(figma_url)

@mcp.tool()
def setFigmaToken(token: str) -> str:
    """Set the Figma API token for the current session."""
    set_figma_token(token)
    return "Figma token set successfully."

# Run the server
if __name__ == "__main__":
    mcp.run(transport="sse")