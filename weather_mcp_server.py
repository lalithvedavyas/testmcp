from fastmcp import MCPServer, Tool

class WeatherTool(Tool):
    name = "getWeather"
    description = "Returns the current weather for a city"

    async def run(self, city: str) -> str:
        return f"The weather in {city} is sunny and 75°F."

server = MCPServer()
server.add_tool(WeatherTool())

if __name__ == "__main__":
    server.run(port=5000)
