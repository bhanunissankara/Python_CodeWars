def draw_stairs(n):
    return '\n'.join([' ' * i + 'I' for i in range(n)])

    # Original Implementation
    # i = 0
    # str1 = ''
    # while i < n:
    #     j = 0
    #     while j <= i:
    #         str1 += ' '
    #         j += 1
    #     str1 += 'I' + '\n'
    #     i += 1
    # return str1
print(draw_stairs(5))