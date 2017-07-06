from weather import *
import pytest

def test_invalid_input():
    city = get_city()
    assert city == 'string'