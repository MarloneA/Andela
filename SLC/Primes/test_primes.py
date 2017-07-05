""" Using the pytest framework """

#import modules
from primes import *
import py.test
    
def test_invalid_input():
    py.test.raises(TypeError, primes, 'string')