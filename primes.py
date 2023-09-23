"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    curr = 2

    while (len(list) < number_of_primes):
        prime = True

        for i in range(2, curr):
            if (curr % i == 0):
                prime = False
                break
        
        if (prime):
            list.append(curr)

        curr += 1

    return list
