def arr(n=0):
        return [j for j in range(n)]


# Traceback (most recent call last):
#   File "/Users/aa619597/Documents/Github/runway-ready-curriculum/python-track/arr_cw.py", line 16, in <module>
#     print(arr())
# TypeError: arr() missing 1 required positional argument: 'n'

# Without using a pre-defined value, Python throws a TypeError. For this, we are pre-defining the value to 0 to
# cater for the no params arr() call

# Check more on Python args and kwargs - "pass a variable number of arguments into a function."


# def arr(n):
#     try:
#         return [j for j in range(n)]
#     except TypeError:
#         return []

print(arr(5))
print(arr(0))
print(arr())