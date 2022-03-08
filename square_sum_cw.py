def square_sum(numbers):
    return sum(list(map(lambda i: i*i,numbers)))

    #First attempt
    # j = 0
    # for i in numbers:
    #     j += i*i
    # return j
# Python Map Lambda
# A lambda expression is a way of creating a little function inline, without all the syntax of a def.
# Here is a lambda with a single n parameter, returning the parameter value doubled.
#
# lambda n: n * 2
# The code of the lambda is typically a single expression without variables or if-statements, and does not use "return".
# Lambda is perfect where you have a short computation to write inline.
# Many programs have some sub-part which can be solved very compactly this way. For longer code, def is better.
#
# The map() function runs a lambda function over the list [1, 2, 3, 4, 5], building a list-like collection of the results, like this:
#
# >>> list(map(lambda n: n * 2, [1, 2, 3, 4, 5]))
# [2, 4, 6, 8, 10]

print(square_sum([0, 3, 4, 5]))
print(square_sum([-1, -2]))