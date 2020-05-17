# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []

    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
                break
            if not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
                break
            else:
                opening_brackets_stack.pop()

    if not opening_brackets_stack:
        return 'Success'
    else:
        return opening_brackets_stack[-1].position + 1



if __name__ == "__main__":
    text = input()
    print(find_mismatch(text))