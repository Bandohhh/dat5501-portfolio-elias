import math
import pytest
from src.increment import increment

def test_increment_happy_path():
    assert increment(4) == 5

@pytest.mark.parametrize("bad", ["4", None, {}, []])
def test_increment_type_errors(bad):
    with pytest.raises(TypeError):
        increment(bad)

@pytest.mark.parametrize("bad_float", [math.inf, -math.inf, math.nan])
def test_increment_rejects_non_finite(bad_float):
    with pytest.raises(ValueError):
        increment(bad_float)


