import pytest
from src.math_ops import add_two # assuming the function is defined in src/math_ops.py

def test_add_two_integers(): # test adding two integers
    assert add_two(2, 3) == 5

def test_add_two_floats(): # test adding two floats
    assert add_two(2.5, 0.5) == 3.0

def test_add_two_mixed_types(): # test adding an integer and a float
    assert add_two(2, 0.5) == 2.5

def test_add_two_raises_on_strings(): # test that adding a string raises TypeError
    with pytest.raises(TypeError):
        add_two("3", 4)

def test_add_two_raises_on_none(): # test that adding None raises TypeError
    with pytest.raises(TypeError):
        add_two(None, 1)
