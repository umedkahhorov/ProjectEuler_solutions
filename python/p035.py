#  all rotations of the digits
#Original string = "197"
#Shift 0 → "197" (no shift)
#Shift 1 → "971" (move the first digit to the end)
#Shift 2 → "719" (move the first two digits to the end)

def sieve_of_eratosthenes(n):
    """
    Generate a list of prime numbers up to n using the Sieve of Eratosthenes.
    """
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
    return prime_numbers

# list comprehension to create all rotations of the digits
num_str = "197"
rotations = [int(num_str[i:] + num_str[:i]) for i in range(len(num_str))]

def chech_if_circular_prime():
    primes_list = sieve_of_eratosthenes(1000000)
    primes_set = set(primes_list)
    get_rotations = lambda x: [int(str(x)[i:] + str(x)[:i]) for i in range(len(str(x)))]
    count = 0
    for p in primes_list:
        rotations = get_rotations(p)
        # Check if every rotated form is still prime
        if all(rot in primes_set for rot in rotations):
            count += 1
    return count




if __name__ == "__main__":
    n = 10**6
    primes = sieve_of_eratosthenes(n)
    print(f"List of primes up to {n}:")
    print(primes[:13])
    print(rotations)
    print(f"Number of circular primes below {n}:")
    print(chech_if_circular_prime())