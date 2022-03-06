def digitize(n):
    arr1 = []
    for i in map(int, str(n)[::-1]):
        arr1.append(i)
    return arr1


print(digitize(23582357))