def group_anagrams(strs):
    dict = {}
    for word in strs:
        key = "".join(sorted(word))
        if key in dict.keys():
            dict[key].append(word)
        else:
            dict[key] = []
            dict[key].append(word)

    return list(dict.values())


test_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(test_strs))