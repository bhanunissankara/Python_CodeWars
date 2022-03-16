"""
You will be given a dictionary, and then you will want to
return a dictionary with the old values as the keys, and list the old keys as values under their original keys.
For example, given the dictionary: {'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'},
you should return: {'Cream': ['Ice', 'Double', 'Light'], '21': ['Age']}
"""

def switch_dict(dic):
    swap_dict = {}
    for key, value in dic.items():
        if swap_dict.get(value) == None:
            swap_dict[value] = [key]
        else:
            swap_dict[value].append(key)

    return swap_dict

print(switch_dict({
          'Ice': 'Cream',
          'Age': '21',
          'Light': 'Cream',
          'Double': 'Cream'
          }))

# from collections import defaultdict
    # res = defaultdict(list)
    # for k, v in dic.items():
    #     res[v].append(k)
