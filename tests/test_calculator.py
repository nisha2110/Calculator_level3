'''This is Calculator Test'''
from calculator import Calculator

def test_addition():
    '''This is addition function test '''    
    assert Calculator.addition1(3,3) == 6

def test_subtraction():
    '''This is substraction function test '''    
    assert Calculator.subtract1(2,2) == 0

def test_multiplication():
    '''This is multiply function test '''
    assert Calculator.multiply(3,3) == 9

def test_division():
    '''This is division function test '''
    assert Calculator.divide(3,3) == 1
    