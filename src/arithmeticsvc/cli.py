import asyncio
from typing import Annotated

import typer

from arithmeticsvc.arithmetic import (
    ArithmeticService,
    ArithmeticServiceConfigs,
    OutputBase,
)
from arithmeticsvc.client import ArithmeticClient

app = typer.Typer()


@app.command()
def add(ctx: typer.Context, left: int, right: int) -> None:
    """
    Adds two numbers.
    """
    service: ArithmeticService = ctx.obj
    result = service.add(left, right)
    typer.echo(result)


@app.command()
def subtract(ctx: typer.Context, left: int, right: int) -> None:
    """
    Subtracts two numbers.
    """
    service: ArithmeticService = ctx.obj
    result = service.subtract(left, right)
    typer.echo(result)


@app.command()
def multiply(ctx: typer.Context, left: int, right: int) -> None:
    """
    Multiplies two numbers.
    """
    service: ArithmeticService = ctx.obj
    result = service.multiply(left, right)
    typer.echo(result)


@app.command()
def integer_divide(ctx: typer.Context, left: int, right: int) -> None:
    """
    Divides two numbers and returns the integer result.
    """
    service: ArithmeticService = ctx.obj
    result = service.integer_divide(left, right)
    typer.echo(result)


@app.callback()
def main(
    ctx: typer.Context,
    output: Annotated[
        OutputBase,
        typer.Option(
            "--output",
            "-o",
            help="The output type to use.",
            show_choices=True,
            show_default=True,
        ),
    ] = OutputBase.decimal,
) -> None:
    """
    A simple CLI for arithmetic operations.
    """
    config = ArithmeticServiceConfigs(OUTPUT_TYPE=output)
    ctx.obj = ArithmeticService(config)


web_app = typer.Typer()

app.add_typer(web_app, name="web")


@web_app.callback()
def web_main(
    ctx: typer.Context,
    host: Annotated[
        str, typer.Option("--host", "-h", help="The host to use.")
    ] = "localhost",
    port: Annotated[int, typer.Option("--port", "-p", help="The port to use.")] = 8000,
) -> None:
    """
    A simple CLI for arithmetic operations.
    """
    ctx.obj = ArithmeticClient(host, port)


@web_app.command(name="add")
def web_add(ctx: typer.Context, left: int, right: int) -> None:
    """
    Adds two numbers.
    """
    client: ArithmeticClient = ctx.obj
    result = asyncio.run(client.add(left, right))
    typer.echo(result)


@web_app.command(name="subtract")
def web_subtract(ctx: typer.Context, left: int, right: int) -> None:
    """
    Subtracts two numbers.
    """
    client: ArithmeticClient = ctx.obj
    result = asyncio.run(client.subtract(left, right))
    typer.echo(result)


@web_app.command(name="multiply")
def web_multiply(ctx: typer.Context, left: int, right: int) -> None:
    """
    Multiplies two numbers.
    """
    client: ArithmeticClient = ctx.obj
    result = asyncio.run(client.multiply(left, right))
    typer.echo(result)


@web_app.command(name="integer_divide")
def web_integer_divide(ctx: typer.Context, left: int, right: int) -> None:
    """
    Divides two numbers and returns the integer result.
    """
    client: ArithmeticClient = ctx.obj
    result = asyncio.run(client.integer_divide(left, right))
    typer.echo(result)


@web_app.command(name="output")
def web_output(ctx: typer.Context, output_type: OutputBase) -> None:
    """
    Changes the output type for the results of the arithmetic operations.
    """
    client: ArithmeticClient = ctx.obj
    result = asyncio.run(client.output(output_type))
    typer.echo(result)


if __name__ == "__main__":
    app()
