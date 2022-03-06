def to_alternating_case(string):
    alternating_case_string = ''
    for i in string:
        if i == i.upper():
            alternating_case_string += i.lower()
        else:
            alternating_case_string += i.upper()

    return alternating_case_string

print(to_alternating_case("hello world"))
print(to_alternating_case("HELLO WORLD"))
print(to_alternating_case("hello WORLD"))
print(to_alternating_case("HeLLo WoRLD"))
print(to_alternating_case("12345"))
print(to_alternating_case("1a2b3c4d5e"))
print(to_alternating_case("String.prototype.toAlternatingCase"))

#     return ''.join([c.upper() if c.islower() else c.lower() for c in string])