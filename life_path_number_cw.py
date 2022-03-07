def life_path_number(birthdate):
    ln = 11
    while ln > 9:
        bday_arr = [int(i) for i in birthdate if i != '-']
        ln = sum(bday_arr)
        birthdate = [int(i) for i in str(ln)]

    return ln



print(life_path_number("1955-10-28"))
print(life_path_number("1971-06-28"))