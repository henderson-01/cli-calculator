"""A simple calculator with a Rich-based CLI interface."""

from rich import box
from rich.box import ROUNDED
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text

console = Console()


def add(x, y):
    """Add two numbers."""
    return x + y


def subtract(x, y):
    """Subtract second number from first."""
    return x - y


def multiply(x, y):
    """Multiply two numbers."""
    return x * y


def divide(x, y):
    """Divide first number by second."""
    if y == 0:
        return "Error! Division by zero."
    return x / y


OPERATIONS = {
    "1": {"name": "Add", "symbol": "+", "func": add, "color": "green"},
    "2": {"name": "Subtract", "symbol": "-", "func": subtract, "color": "red"},
    "3": {"name": "Multiply", "symbol": "×", "func": multiply, "color": "blue"},
    "4": {"name": "Divide", "symbol": "÷", "func": divide, "color": "yellow"},
}


def display_welcome():
    """Display the welcome banner."""
    welcome_text = Text()
    welcome_text.append("Simple", style="bold cyan")
    welcome_text.append(" Calculator", style="bold white")

    console.print()
    console.print(
        Panel(
            welcome_text,
            title="[bold magenta]🧮 Welcome[/bold magenta]",
            subtitle="[dim]A beautiful calculator experience[/dim]",
            border_style="cyan",
            box=ROUNDED,
        )
    )


def display_operations():
    """Display available operations in a table."""
    table = Table(
        title="Available Operations",
        box=box.ROUNDED,
        border_style="blue",
        show_header=True,
        header_style="bold magenta",
    )

    table.add_column("Key", style="cyan", justify="center", width=6)
    table.add_column("Operation", style="green", justify="left")
    table.add_column("Symbol", style="yellow", justify="center", width=8)

    for key, op in OPERATIONS.items():
        table.add_row(key, op["name"], op["symbol"])

    console.print(table)


def get_user_input():
    """Get and validate user input."""
    while True:
        choice = Prompt.ask(
            "\n[bold]Select operation[/bold] [green](Keys)[/green]",
            choices=["1", "2", "3", "4"],
            default="Default 1",  # Default to '1' if no input is provided
        )

        if choice in OPERATIONS:
            break
        console.print("[red]Invalid choice. Please enter 1-4.[/red]")

    while True:
        try:
            num1 = float(Prompt.ask("[bold]Enter first number[/bold]"))
            num2 = float(Prompt.ask("[bold]Enter second number[/bold]"))
            break
        except ValueError:
            console.print("[red]Invalid input. Please enter valid numbers.[/red]")

    return choice, num1, num2


def display_result(choice, num1, num2, result):
    """Display the calculation result in a styled panel."""
    op = OPERATIONS[choice]

    if isinstance(result, str):
        # Error message
        console.print()
        console.print(
            Panel(
                f"[bold red]⚠️ {result}[/bold red]",
                title="[bold red]Error[/bold red]",
                border_style="red",
                box=ROUNDED,
            )
        )
    else:
        # Format the result
        if result == int(result):
            result_str = str(int(result))
        else:
            result_str = f"{result:.4f}".rstrip("0").rstrip(".")

        calculation_text = Text()
        calculation_text.append(f"{num1} ", style="white")
        calculation_text.append(f"{op['symbol']} ", style=f"bold {op['color']}")
        calculation_text.append(f"{num2} ", style="white")
        calculation_text.append("= ", style="white")
        calculation_text.append(result_str, style="bold green")

        console.print()
        console.print(
            Panel(
                calculation_text,
                title=f"[bold]{op['name']} Result[/bold]",
                border_style=op["color"],
                box=ROUNDED,
            )
        )


def calculator():
    """Main calculator function."""
    display_welcome()
    display_operations()

    choice, num1, num2 = get_user_input()

    op = OPERATIONS[choice]
    result = op["func"](num1, num2)

    display_result(choice, num1, num2, result)

    console.print()
    console.print("[dim]Thank you for using the calculator! 🎉[/dim]\n")


if __name__ == "__main__":
    calculator()
