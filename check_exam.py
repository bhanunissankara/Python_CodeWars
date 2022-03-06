def check_exam(arr1, arr2):
    marks = 0
    for i, option in enumerate(arr1):
        if arr2[i] == '':
            continue
        elif arr2[i] == arr1[i]:
            marks += 4
        else:
            marks = marks - 1

    return 0 if marks < 0 else marks


print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))