"""
prime.py -- Write the application code here
"""
def generate_prime_factors(n):
    if isinstance(n, int):
        i=2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n//= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors
    else:
        return []
