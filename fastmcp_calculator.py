from fastmcp import FastMCP

mcp = FastMCP(name = 'Calculator')

@mcp.tool()
def multiply (a: float, b: float) -> float:
    """Multiple two numbers.
    
    args: a (float) is the first number
          b (float) is the second number


    returns: float: The product of two numbers
    """
    return a*b

@mcp.tool(
    name = "add",
    description = "Add two numbers.",
    tags = ["math", "arithmetic"]
)

def add_numbers(x: float ,y: float) -> float:
    """Add two numbers.
    
    args: a (float) is the first number
          b (float) is the second number

    returns: float: The sum of two numbers.
    """
    return x + y

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers
    
    args: a (float): The first number.
          b (float): The second number.

    returns: float: THe difference of the two numbers.
    """
    return a - b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers
    
    args: a (float): The first number.
          b (float): The second number.

    returns: float: The quoteint of two numbers.
    """
    if b == 0:
        raise ValueError("Can not divide by zero.")
    return a/b

if __name__ == "__main__":
    mcp.run() #STDIO by default