def sum_of_intervals(intervals):
    sum = 0
    arr1 = []
    for i, values in intervals:
        for j in intervals:
            in_range = False
            first_element = j[0]
            second_element = j[1]
            if i[0] in range(first_element, second_element):
                in_range = True

    return sum

print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))