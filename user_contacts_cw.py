# You're putting together contact information for all the users of your website to ship them a small gift.
# You queried your database and got back a list of users, where each user is another list with up to
# two items: a string representing the user's name and their shipping zip code. Example data might look like:

def user_contacts(data):
    user_dict = {}
    for i in data:
        print(len(i))
        if len(i) < 2:
            user_dict[i[0]] = None
        else:
            user_dict[i[0]] = i[1]

    return user_dict

    # a = {}
    # for i in data:
    #     a[i[0]] = i[1] if len(i) == 2 else None
    # return a

print(user_contacts([["Grae Drake", 98110], ["Bethany Kok"], ["Alex Nussbacher", 94101], ["Darrell Silver", 11201]]))