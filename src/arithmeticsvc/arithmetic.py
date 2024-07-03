from enum import Enum

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class OutputBase(str, Enum):
    """
    Defines all possible output options for the results of the arithmetic operations.
    """

    binary = "bin"
    octal = "oct"
    decimal = "dec"
    hexadecimal = "hex"


class ArithmeticServiceConfigs(BaseSettings):
    """
    A class to hold the configurations for the arithmetic service.

    Attributes:
      output_type: The output type for the results of the arithmetic operations.
    """

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_prefix="ARITHMETIC_",
        env_file=".env",
    )
    OUTPUT_TYPE: OutputBase = Field(default="dec")


class ArithmeticService:
    """
    A simple arithmetic service to showcase how to reuse a service
    configuration for CLIs and web services.
    """

    config: ArithmeticServiceConfigs

    def __init__(self, config: ArithmeticServiceConfigs):
        self.config = config

    def add(self, left: int, right: int) -> str:
        """
        Adds two numbers and returns the result in the output type specified in the configuration.
        """
        result = left + right
        return self._format_result(result)

    def subtract(self, left: int, right: int) -> str:
        """
        Subtracts two numbers and returns the result in the output type specified in the configuration.
        """
        result = left - right
        return self._format_result(result)

    def multiply(self, left: int, right: int) -> str:
        """
        Multiplies two numbers and returns the result in the output type specified in the configuration.
        """
        result = left * right
        return self._format_result(result)

    def integer_divide(self, left: int, right: int) -> str:
        """
        Divides two numbers and returns the result in the output type specified in the configuration.
        """
        result = left // right

        return self._format_result(result)

    def _format_result(self, result: int) -> str:
        """
        Formats the result based on the output type specified in the configuration.
        """

        if self.config.OUTPUT_TYPE == OutputBase.binary:
            return bin(result)
        elif self.config.OUTPUT_TYPE == OutputBase.octal:
            return oct(result)
        elif self.config.OUTPUT_TYPE == OutputBase.decimal:
            return str(result)
        elif self.config.OUTPUT_TYPE == OutputBase.hexadecimal:
            return hex(result)
        else:
            raise ValueError(f"Unsupported output type: {self.config.OUTPUT_TYPE}")
