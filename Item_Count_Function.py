import time

def count_items(items):
    result = {}
    for item in items:
        result[item] = result.get(item, 0) + 1
    return result

def num_of_chars(input_str):
    start_time = time.process_time()
    upper_str = ''
    lower_srt = ''
    all_chars = ''.join(i for i in input_str.split() if i.isalnum())
    for i in input_str:
        if i == ' ' or i =='.':
            continue
        elif i == i.upper():
            upper_str += i
        else:
            lower_srt += i
    print("Upper Chars", count_items(upper_str))
    print("Lower Chars", count_items(lower_srt))
    print("All chars", count_items(all_chars))
    end_time = time.process_time()
    print(end_time - start_time)

num_of_chars("Juno is the best. JUNO.")
print(count_items([1, 2, 3, 3, 4]))
print(count_items([True, False, False, True, True]))