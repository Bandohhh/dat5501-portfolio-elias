'''print('How old are you? ')
print('What is your name? ')
print('What is your favorite color? ') ''' 

import pytest
from src.math_ops import add_two

def test_add_two_integers():
    assert add_two(2, 3) == 5

def test_add_two_floats():
    assert add_two(2.5, 0.5) == 3.0

def test_add_two_mixed_types():
    assert add_two(2, 0.5) == 2.5

def test_add_two_raises_on_strings():
    with pytest.raises(TypeError):
        add_two("3", 4)

def test_add_two_raises_on_none():
    with pytest.raises(TypeError):
        add_two(None, 1)
