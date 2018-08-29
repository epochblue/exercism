import math


def aliquot_sum(number):
    factors = set()
    upper_bound = int(math.sqrt(number))
    for i in range(1, upper_bound + 1):
        if number % i == 0:
            factors.update([i, number//i])
    factors.remove(number)
    return sum(factors)

def classify(number):
    if number <= 0:
        raise ValueError('Cannot classify this number.')

    a_sum = aliquot_sum(number)

    if a_sum == number:
        return 'perfect'
    if a_sum > number:
        return 'abundant'
    return 'deficient'

