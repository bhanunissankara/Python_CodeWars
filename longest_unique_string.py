# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string,
# the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.


def longest(a, b):
    return_str = ""
    for element in a:
        if element not in return_str:
            return_str = return_str + element
    for element in b:
        if element not in return_str:
            return_str = return_str + element
    #return(''.join(map(str, sorted(return_str))))
    return(''.join(sorted(return_str)))

print(longest("owen", "shen"))


#def longest(a1, a2):
#    return "".join(sorted(set(a1 + a2)))
