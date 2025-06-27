# weather_mcp_server.py
from fastmcp import FastMCP

mcp = FastMCP(name="Weather MCP Server")

@mcp.tool
def get_weather(city: str) -> str:
    """Returns mock weather info for the given city."""
    return f"The weather in {city} is sunny and 75°F."

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=5000, path="/mcp")
