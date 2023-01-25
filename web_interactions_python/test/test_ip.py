"""Tests ip_functions module"""

import unittest
from webinteractions import get_ipv4address_generator, get_ipv6address_generator

class IPTestMethods(unittest.TestCase):
    """Class tests the ip_functions module"""
    
    def test_ipv4_address(self):
        generator = get_ipv4address_generator("192.168.0.0/30")
        self.assertEqual(len(generator), 2)


if __name__ == "__main__":
    unittest.main()
