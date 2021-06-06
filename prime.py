"""
prime.py -- Write the application code here
"""

def generate_prime_factors(n):
    if isinstance(n, int):
        i = 2
        factors = []
        if n > 1:
            factors.append(n)
        return factors
    else:
        return []
