def ends_with_ab(string):
    state = 0  
    for char in string:
        if state == 0:
            if char == 'a':
                state = 1
            else:
                state = 0
        elif state == 1:
            if char == 'a':
                state = 1
            elif char == 'b':
                state = 2
            else:
                state = 0
        elif state == 2:
            if char == 'a':
                state = 1
            else:
                state = 0
    return state == 2
test_strings = ["ab", "aab", "cab", "abab", "aba", "bba", "aaab"]
for s in test_strings:
    if ends_with_ab(s):
        print(f"{s} -> Accepted")
    else:
        print(f"{s} -> Rejected")
