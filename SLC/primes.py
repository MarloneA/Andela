def primes(n):
    if n < 2:
        return 'No primes in range'
    else: # when is 2 or greater
        all_primes_in_range = [2] # 2 is our first prime
        for i in range(3, n + 1): # we test primality from 3 to n
            if n % 2 == 0:
                continue # eliminate even numbers greater than 2
            else:
                # reduce n by checking only odd numbers greater than 2
        return all_primes_in_range