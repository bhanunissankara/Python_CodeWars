# Facebook logo stickers cost $2 each from the company store. I have an idea.
# I want to cut up the stickers, and use the letters to make other words/phrases.
# A Facebook logo sticker contains only the word 'facebook', in all lower-case letters.
#
# Write a function that, given a string consisting of a word or words made up
# of letters from the word 'facebook', outputs an integer with the number of
# stickers I will need to buy.
#
# get_num_stickers('coffee kebab') -> 3
# get_num_stickers('book') -> 1
# get_num_stickers('ffacebook') -> 2
#
# You can assume the input you are passed is valid, that is, does not contain
# any non-'facebook' letters, and the only potential non-letter characters
# in the string are spaces.

def count_items(items):
    result = {}
    for item in items:
        result[item] = result.get(item, 0) + 1
    return result

def fb_map_update(fb_map):
    fb_map['f'] = fb_map['f'] + 1
    fb_map['a'] = fb_map['a'] + 1
    fb_map['c'] = fb_map['c'] + 1
    fb_map['e'] = fb_map['e'] + 1
    fb_map['b'] = fb_map['b'] + 1
    fb_map['o'] = fb_map['o'] + 2
    fb_map['k'] = fb_map['k'] + 1

    return fb_map

def stickers(name):
    sticker_count = 1
    fb_map = count_items("facebook")
    for letter in name:
        if fb_map[letter] == 0:
            sticker_count += 1
            fb_map_update(fb_map)
        else:
            fb_map[letter] -= 1

    return sticker_count

print(stickers('coffeekebab')) # -> 3
print(stickers('book')) # -> 1
print(stickers('ffacebook')) # -> 2
