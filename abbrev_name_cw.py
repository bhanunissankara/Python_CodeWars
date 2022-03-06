def abbrev_name(name):
    i = name.split()
    ab_name = ''
    for i, name in enumerate(i):
        if i == 0:
            ab_name = name[0].upper()
        else:
            ab_name += '.' + name[0].upper()

    return ab_name


print(abbrev_name("Sam Harris Main"))
print(abbrev_name("patrick feenan"))
print(abbrev_name("Evan C"))
print(abbrev_name("P Favuzzi"))
print(abbrev_name("David Mendieta"))

#     return '.'.join(w[0] for w in name.split()).upper()

# first, last = name.upper().split(' ')
# return first[0] + '.' + last[0]