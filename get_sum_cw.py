def get_sum(a, b):
    a_b = sorted([a, b])
    return sum(i for i in range(a_b[0], a_b[1] + 1))

#     sum = 0
#     if a<b:
#         for i in range(a,b+1):
#             sum += i
#     else:
#         for i in range(b,a+1):
#             sum += i

#     return sum
# good luck!
#     if a>b : a,b = b,a
#     return sum(range(a,b+1))