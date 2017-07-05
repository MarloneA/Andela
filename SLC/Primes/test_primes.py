""" Using the unittest framework """

# Test cases:
# integer input. should be a number
# input greater or equal to 2
# is_prime (only two factors: 1 and self) - primality

from primes import *
import unittest

class TestPrimes(unittest.TestCase):
    
    def test_invalid_input(self):
        self.assertRaises(TypeError, primes, 'string')

if __name__ == '__main__':
    unittest.main()