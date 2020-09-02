import datetime


def is_prime_slow(num):
    if num < 2:
        return False
    if num == 2:
        return True

    cur = 2
    while cur < num:
        if num % cur == 0:
            return False
        cur += 1

    return True


def is_prime_fast(num, cache):
    if num in cache:
        return cache[num]

    if num < 2:
        return False
    if num == 2:
        return True

    cur = 2
    while cur < num:
        if num % cur == 0:
            cache[num] = False
            return False
        cur += 1

    cache[num] = True
    return True


# num = int(input(f"Enter a number to test: "))
# print(is_prime(num))

def test_primes():
    num = int(input(f"Enter max number to test: "))

    # slow
    start = datetime.datetime.now()
    primes = []
    for i in range(num):
        if is_prime_slow(i):
            primes.append(i)
    end = datetime.datetime.now()
    print(str(end-start))

    # slow
    start = datetime.datetime.now()
    primes = []
    cache = {}
    for i in range(num):
        if is_prime_fast(i, cache):
            primes.append(i)
    end = datetime.datetime.now()
    print(str(end-start))


# print(primes)
test_primes()
