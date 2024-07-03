import pytest

from arithmeticsvc.arithmetic import (
    ArithmeticService,
    ArithmeticServiceConfigs,
    OutputBase,
)


@pytest.fixture
def config() -> ArithmeticServiceConfigs:
    return ArithmeticServiceConfigs()


def test_add(config: ArithmeticServiceConfigs):
    service = ArithmeticService(config)
    assert service.add(1, 2) == "3"


def test_subtract(config: ArithmeticServiceConfigs):
    service = ArithmeticService(config)
    assert service.subtract(3, 2) == "1"


def test_multiply(config: ArithmeticServiceConfigs):
    service = ArithmeticService(config)
    assert service.multiply(3, 2) == "6"


def test_integer_divide(config: ArithmeticServiceConfigs):
    service = ArithmeticService(config)
    assert service.integer_divide(5, 2) == "2"


def test_add_bin(config: ArithmeticServiceConfigs):
    config.OUTPUT_TYPE = OutputBase.binary
    service = ArithmeticService(config)
    assert service.add(1, 2) == "0b11"
