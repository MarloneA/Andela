def fizz_buzz(i):

    if i > 0: # only positives
        if i % 3 == 0 and i % 5 == 0:
            return 'fizzBuzz'
        elif i % 3 == 0:
            return 'fizz'
        elif i % 5 == 0:
            return 'buzz'
        else:
            return i
    else: # 0 or less
        return 'Invalid Argument'

fizz_buzz(1)