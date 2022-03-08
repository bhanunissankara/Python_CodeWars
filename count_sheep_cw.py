def count_sheep(n):
    return ''.join(str(i)+' sheep...' for i in range(1,n+1,1))

print(count_sheep(2))