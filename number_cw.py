def number(lines):
    if not lines:
        return []
    return ('x'.join(str(i+1)+': '+j for i, j in enumerate(lines))).split('x')

    # arr1 = []
    # for i, j in enumerate(lines):
    #     arr1.append(str(i+1) + ': ' + j)
    #
    # return arr1

print(number(["a", "b", "c"]))
print(number([]))