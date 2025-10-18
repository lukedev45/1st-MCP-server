#HTTP
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

# 1. Making a fastapi app

app =FastAPI(title="MCP Calcualtor with API")

@app.post("/multiply")
def multiply (a: float, b: float):
    """Multiple two numbers."""
    return a*b

@app.post("/add")
def add (a: float, b: float):
    """Add two numbers"""
    return a + b

@app.post("/subtract")
def subtract(a: float, b: float):
    """Subtract two numbers"""
    return a - b

@app.post("/divide")
def divide(a: float, b: float):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Can not divide by zero.")
    return a/b

# 2. Convert to MCP app

mcp = FastApiMCP(app, name="Calculator API MCP")
mcp.mount_http()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8002)