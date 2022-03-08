def multi_table(number):
    table = ''
    for i in range(1,11):
        table += str(i) + ' * ' + str(number) + ' = ' + str(i*number) + '\n'
    return table.rstrip('\n')

# return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))
# table += f'{i} * {number} = {i*number}\n'
print(multi_table(10))