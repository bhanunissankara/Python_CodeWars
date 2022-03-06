def first_non_consecutive(arr):
   for i, num in enumerate(arr):
           if i+1 == len(arr):
               return None
           elif num + 1 == arr[i+1]:
               continue
           else:
               return arr[i+1]

print(first_non_consecutive([1,2,3,4,6,7,8]))