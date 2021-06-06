# pylint: disable=missing-docstring
"""
The test module for Prime Factors
"""
import prime

def test_generate_prime_factors():
    """ Pass when not Int """
    assert prime.generate_prime_factors("16") == []
def test_2_generate_prime_factors():
    """ empty list """
    assert prime.generate_prime_factors(1) == []
