"""
This module contains unit tests for the calculator's basic operations
including addition, subtraction, multiplication, and division.
"""
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import addition1, subtract1, multiply, divide

@pytest.mark.parametrize("operand1, operand2, operation, expected", [
    (Decimal('10'), Decimal('5'), addition1, Decimal('15')),  # Test addition
    (Decimal('10'), Decimal('5'), subtract1, Decimal('5')),  # Test subtraction
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),  # Test multiplication
    (Decimal('10'), Decimal('2'), divide, Decimal('5')),  # Test division
    (Decimal('10.5'), Decimal('0.5'), addition1, Decimal('11.0')),  # Test addition with decimals
    (Decimal('10.5'), Decimal('0.5'), subtract1, Decimal('10.0')),  # Test subtraction with decimals
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),  # Test multiplication with decimals
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),  # Test division with decimals
])
def test_calculation_operations(operand1, operand2, operation, expected):
    """
    Test calculation operations with various scenarios.
    """
    calc = Calculation(operand1, operand2, operation)
    assert calc.perform() == expected, \
        f"Failed {operation.__name__} operation with {operand1} and {operand2}"

def test_calculation_repr():
    """
    Test the __repr__ method of the Calculation class.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), addition1)
    expected_repr = "Calculation(10, 5, addition1)"
    assert repr(calc) == expected_repr, "The repr() output doesn't match the expected string."
def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        # Attempt to perform the calculation, which should trigger the ValueError.
        calc.perform()
