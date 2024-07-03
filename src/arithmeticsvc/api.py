from typing import Annotated
from contextlib import asynccontextmanager

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

from arithmeticsvc.arithmetic import (
    ArithmeticService,
    ArithmeticServiceConfigs,
    OutputBase,
)


class Operands(BaseModel):
    """
    A class to hold the data for an arithmetic operation.
    """

    left: int = Field(
        ...,
        title="The first number.",
        description="The first number to use in the arithmetic operation.",
    )
    right: int = Field(
        ...,
        title="The second number.",
        description="The second number to use in the arithmetic operation.",
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Initializes the arithmetic service.
    """
    app.state.service = ArithmeticService(ArithmeticServiceConfigs())  # type: ignore
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/add")
async def add(
    operation: Annotated[Operands, Body(..., title="The operands for the operation")],
):
    """
    Adds two numbers.
    """
    service: ArithmeticService = app.state.service
    result = service.add(operation.left, operation.right)
    return {"result": result}


@app.post("/subtract")
async def subtract(
    operation: Annotated[Operands, Body(..., title="The operands for the operation")],
):
    """
    Subtracts two numbers.
    """
    service: ArithmeticService = app.state.service
    result = service.subtract(operation.left, operation.right)
    return {"result": result}


@app.post("/multiply")
async def multiply(
    operation: Annotated[Operands, Body(..., title="The operands for the operation")],
):
    """
    Multiplies two numbers.
    """
    service: ArithmeticService = app.state.service
    result = service.multiply(operation.left, operation.right)
    return {"result": result}


@app.post("/integer_divide")
async def integer_divide(
    operation: Annotated[Operands, Body(..., title="The operands for the operation")],
):
    """
    Divides two numbers and returns the integer result.
    """
    service: ArithmeticService = app.state.service
    result = service.integer_divide(operation.left, operation.right)
    return {"result": result}


@app.get("/output/{output_type}")
async def output(output_type: OutputBase):
    """
    Changes the output type for the results of the arithmetic operations.
    """
    config: ArithmeticServiceConfigs = app.state.service.config
    config.OUTPUT_TYPE = output_type
    return {"output_type": output_type}
