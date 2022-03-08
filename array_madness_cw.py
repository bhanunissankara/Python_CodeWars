def array_madness(arr1,arr2):
    return sum(map(lambda n: n*n, arr1)) > sum(map(lambda n: n*n*n, arr2))

print(array_madness([4, 5, 6], [1, 2, 3]))