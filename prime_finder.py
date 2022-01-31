from math import sqrt


def is_it_prime(n):
    k = int(sqrt(n))
    for i in range(2, k + 1):
        if n % i == 0:  # checking if i divides n
            return False
    return True


def prime_finder(n):
    result = []
    for i in range(2, n + 1):
        if is_it_prime(i) == True:
            result.append(i)
    return result


print(prime_finder(10))
