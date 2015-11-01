def sieve(limit):
    """
    Return a list of prime numbers up to the given limit using the
    Sieve of Eratosthenes algorithm.
    """
    primes = []
    non_primes = set()

    for i in xrange(2, limit+1):
        if i not in non_primes:
            primes.append(i)

            for a in xrange(i*i, limit+1, i):
                non_primes.add(a)
    return primes
