def find_multiples(integer, limit):
    return [ integer * (j+1) for j in range((int(limit/integer)).__floor__())]

print(find_multiples(5, 25))