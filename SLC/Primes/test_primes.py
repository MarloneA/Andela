""" Using the unittest framework """

#import modules
from primes import *
import unittest

class TestPrimes(unittest.TestCase):
    
    def test_invalid_input(self):
        self.assertRaises(TypeError, primes, 'string')

if __name__ == '__main__':
    unittest.main()