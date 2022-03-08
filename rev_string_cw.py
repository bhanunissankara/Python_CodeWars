def solution(string):
    return ''.join([i for i in string][::-1])

print(solution('world'))