def divisors(integer):
    l = [a for a in range(2, integer) if integer%a == 0]
    if l:
        return l
    else:
        return str(integer) + " is prime"
