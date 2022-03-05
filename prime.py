def divisors(integer):
    i = 2
    return_list = []
    while (i < integer):
        result = integer/i
        if result.is_integer():
            return_list.append(i)
        i = i + 1
    if return_list:
        return return_list
    else:
        return str(integer) + " is prime"

print(divisors(7))


# Create a function named divisors/Divisors that takes an integer n > 1
# and returns an array with all of the integer's divisors(except for 1
# and the number itself), from smallest to largest. If the number is prime
# return the string '(integer) is prime' (null in C#) (use Either String a
# in Haskell and Result<Vec<u32>, String> in Rust).

# divisors(12); #should return [2,3,4,6]
# divisors(25); #should return [5]
# divisors(13); #should return "13 is prime"

#def divisors(integer):
#  return [n for n in range(2, integer) if integer % n == 0] or '{} is prime'.format(integer)

#def divisors(num):
#    l = [a for a in range(2,num) if num%a == 0]
#    if len(l) == 0:
#        return str(num) + " is prime"
#    return l
