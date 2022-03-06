def to_csv_text(array):
    text = ''
    l = len(array)
    for l1, i in enumerate(array):
        l2 = len(i)
        for l3, j in enumerate(i):
            if l3 < l2 - 1:
                text += ''.join(str(j)) + ','
            else:
                text += ''.join(str(j))
        if l1 != l - 1:
            text += '\n'

    return text


print(to_csv_text([
    [0, 1, 2, 3, 45],
    [10, 11, 12, 13, 14],
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34]
]))