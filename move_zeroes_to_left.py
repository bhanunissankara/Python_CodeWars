"""
Given an integer array, move all elements that are 0 to the left while maintaining the order of other elements in the array.
The array has to be modified in-place. Try it yourself before reviewing the solution and explanation.
"""

def move_zeros_to_left(A):
  num_of_zeroes = 0
  for index, value in enumerate(A):
    if value == 0:
      A.pop(index)
      num_of_zeroes += 1
  while num_of_zeroes > 0:
    A.insert(0,0)
    num_of_zeroes -= 1
  return A

print(move_zeros_to_left([1,10,20,0,59,63,0,88,0]))