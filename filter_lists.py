def filter_list(l):
  return_list = []
  for element in l:
    if(type(element) == int):
        return_list.append(element)
  return return_list

# Output should be a list of integer numbers
# test.assert_equals(filter_list([1,2,'a','b']),[1,2])
# test.assert_equals(filter_list([1,'a','b',0,15]),[1,0,15])
# test.assert_equals(filter_list([1,2,'aasf','1','123',123]),[1,2,123])

# Also:
#def filter_list(l):
#  'return a new list with the strings filtered out'
#  return [i for i in l if not isinstance(i, str)]
