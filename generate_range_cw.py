def generate_range(min, max, step):
    arr1 = []
    while min <= max:
        arr1.append(min)
        min += step
    return arr1

print(generate_range(1, 10, 1))
print(generate_range(-10, 1, 1))