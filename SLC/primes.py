def primes(n):
    if n < 2:
        return 'No primes in range'
    else: # when is 2 or greater
        all_primes_in_range = [2] # 2 is our first prime
        for i in range(3, n + 1): # we test primality from 3 to n
            # run the primality test here and add only primes to the list to be returned
        return all_primes_in_range