# Make 'src' importable without tricky packages
import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))

import pytest
from increment import inc

def test_inc_happy_path():
    assert inc(4) == 5


@pytest.mark.parametrize("bad", ["4", None, {}, []])
def test_inc_type_errors(bad):
    with pytest.raises(TypeError):
        inc(bad)

