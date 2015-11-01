def sieve(limit):
    """
    Return a list of prime numbers up to the given limit using the
    Sieve of Eratosthenes algorithm.
    """
    numbers = list(xrange(2, limit+1))
    for i in numbers:
        for a in numbers:
            if i != a and a % i == 0:
                numbers.remove(a)

    return numbers
