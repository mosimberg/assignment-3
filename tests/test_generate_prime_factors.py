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
def test_3_generate_prime_factors():
    """ Pass with 1 item """
    assert prime.generate_prime_factors(2) == [2]
def test_4_generate_prime_factors():
    """ Pass with correct factors """
    assert prime.generate_prime_factors(3) == [3]
def test_5_generate_prime_factors():
    assert prime.generate_prime_factors(4) == [2, 2]
def test_6_generate_prime_factors():
    assert prime.generate_prime_factors(6) == [2, 3]
def test_7_generate_prime_factors():
    assert prime.generate_prime_factors(8) == [2, 2, 2]
def test_8_generate_prime_factors():
    assert prime.generate_prime_factors(9) == [3,3]
