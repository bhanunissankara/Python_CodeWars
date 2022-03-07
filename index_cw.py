def index(array, n):
    return pow(array[n],n) if n < len(array) else -1


print(index([1, 2, 3, 4],9))
print(index([1, 2, 3, 4],2))