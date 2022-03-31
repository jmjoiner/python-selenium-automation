def generate_primes_brute_force(n):
    primes = []

    for i in range(2, n + 1):
        for p in range(2, i + 1):
            if p == i:
                primes.append(i)
                break
            if i % p == 0:
                break

    return primes



def generate_primes(n):
    primes = []

    is_prime = [False, False] + [True] * (n - 1)

    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p, n + 1, p):
                is_prime[i] = False

    return primes


test_n18 = 18
test_n = 8

print('Brute force solution: ')
print(generate_primes_brute_force(test_n))
print(generate_primes_brute_force(test_n18))

print('Smart solution: ')
print(generate_primes(test_n))
print(generate_primes(test_n18))