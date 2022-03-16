"""
In this example you have to validate if a user input string is alphanumeric.
The given string is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore
"""

def alphanumeric(password):
    allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    if password == "":
        return False
    for i in password:
        print(i.upper())
        if i.upper() not in allowed:
            return False

    return True

print(alphanumeric("hello world_"))
print(alphanumeric("PassW0rd"))

# import re
#
# pattern = re.compile('^[0-9a-zA-Z]+$')
#
# def alphanumeric(string):
#   return pattern.match(string) is not None