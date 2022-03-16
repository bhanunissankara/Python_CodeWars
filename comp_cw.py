import math
def comp(array1, array2):
    print(array1 is None)
    print(array2)
    print(array2 is None)
    if array2 is None:
        return False
    is_same = True
    # Create an array for each number in array2 that can be formed by squaring a number
    square_arr = []
    for j in array2:
        if j == 0:
            square_arr.append(j)
        else:
            for i in range(int(math.ceil(j / 2)) + 1):
                if i * i == j:
                    square_arr.append(i)
    for i in array1:
        if array1.count(i) != square_arr.count(i):
            is_same = False

    return is_same