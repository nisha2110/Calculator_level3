from calculator.calculation import Calculation
from calculator.operations import addition1, subtract1, multiply, divide

class Calculator:
    @staticmethod
    def addition1(a,b):
        calculation = Calculation(a, b, addition1)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def subtract1(a,b):
        calculation = Calculation(a, b, subtract1)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def multiply(a,b):
        calculation = Calculation(a, b, multiply)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def divide(a,b):
        calculation = Calculation(a, b, divide)  # Pass the add function from calculator.operations
        return calculation.get_result()