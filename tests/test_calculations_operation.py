'''This is Calculator Test'''
from calculator.operations import addition1, subtract1, multiply, divide

def test_addition():
    '''This is addition function test '''    
    assert addition1(3,3) == 6
def test_subtraction():
    '''This is substraction function test '''
    assert subtract1(2,2) == 0
def test_multiplication():
    '''This is multiply function test '''
    assert multiply(3,3) == 9
def test_division():
    '''This is division function test '''
    assert divide(3,3) == 1
