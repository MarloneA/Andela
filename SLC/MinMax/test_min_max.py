# import modules
# from min_max import findMinMax
import pytest

def test_invalid_input():
    pytest.raises(TypeError, findMinMax, 'string')

