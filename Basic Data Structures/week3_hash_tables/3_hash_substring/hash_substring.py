# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    output = []
    comp1,comp2, lp, lt = pattern[0], pattern[-1], len(pattern), len(text)
    indices = [x for x in range(lt) if text[x] == comp1 and (x + lp)<= lt]
    for i in indices:
        if text[i+lp-1] == comp2:
            if pattern == text[i:i+lp]:
                output.append(i)
    return output

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))