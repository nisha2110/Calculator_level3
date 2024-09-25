'''This is Calculator Test'''
from calculator import addition1, subtract1

def test_addition():
    '''This is addition function test '''    
    assert addition1(3,3) == 6

def test_subtraction():
    '''This is substraction function test '''    
    assert subtract1(2,2) == 0
    