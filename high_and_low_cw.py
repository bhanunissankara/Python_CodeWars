def high_and_low(numbers):
    num_arr = list(map(int, numbers.split(' ')))
    return str(max(num_arr)) + ' ' + str(min(num_arr))

    # num_arr = [i for i in map(str, sorted(map(int, numbers.split(' '))))]
    # return str(num_arr[-1]) + " " + str(num_arr[0])

#   Partially Working
#   return ' '.join(str(i) for i in sorted([int(i) for i in numbers.split(' ')]))


  # num_arr = []
  # for i in numbers.split(' '):
  #     num_arr.append(int(i))
  # print(num_arr)
  # num_arr.sort()
  # print(num_arr)
  # print(num_arr[::-1])
  #
  # return str(num_arr[-1]) + " " + str(num_arr[0])

# CW Solution
# def high_and_low(numbers):
#   return " ".join(x(numbers.split(), key=int) for x in (max, min))

print(high_and_low("19 -2 0 8 7 1 4 -8 -9"))