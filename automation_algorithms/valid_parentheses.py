def is_valid_parentheses(s):
    parentheses = {'(': ')', '[': ']', '{': '}'}
    control = []

    for i in s:
        if i in parentheses:
            control.append(parentheses[i])
        elif control.pop() != i:
            return False

    if len(control) != 0:
        return False

    return True


test_s_pos = '[{}]()'
test_s_neg = '[{}]{}('

print(is_valid_parentheses(test_s_pos))
print(is_valid_parentheses(test_s_neg))
