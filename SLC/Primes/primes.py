def primes(n):
    if n < 2:
        print 'No primes in range'
    else:
        all_primes_in_range = []
        for i in range(2, n + 1):
            for x in range(2, i):# factorization
                if i % x == 0: # is it divisible by any other number less than it?
                    break
            else:
                all_primes_in_range.append(i)
        print all_primes_in_range