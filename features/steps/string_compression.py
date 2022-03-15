def compress_string(s):
    if len(s) == 0:
        return ""


    if len(s) == 1:
        return s + "1"


    compressed = ""
    cnt = 1
    i = 1

    while i < len(s):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            compressed = compressed + s[i - 1] + str(cnt)
            cnt = 1
        i += 1


    compressed = compressed + s[i - 1] + str(cnt)

    return compressed


test_1 = ""
test_2 = "a"
test_3 = "aaaAAbCCC"
print(compress_string(test_1))
print(compress_string(test_2))
print(compress_string(test_3))