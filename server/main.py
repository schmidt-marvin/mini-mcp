from fastmcp import FastMCP

app = FastMCP()


@app.tool()
def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    app.run(transport="http", host="127.0.0.1", port=8023, path="/mcp")
