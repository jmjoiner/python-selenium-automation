def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    #return sorted(s1) == sorted(s2)
    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True


str_1_pos = "abcde"
str_2_pos = "abced"
print(is_anagram(str_1_pos, str_2_pos))


str_1_neg = "abcde"
str_2_neg = "abceb"
print(is_anagram(str_1_neg, str_2_neg))



