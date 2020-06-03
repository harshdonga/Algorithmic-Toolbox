# python3
import sys

def BWT(text):
    n = len(text)
    out = []
    for i in range(n-1, -1, -1):
        out.append((text[i:]+text[:i]))
    return ''.join(x[-1] for x in sorted(out))
        
if __name__ == '__main__':
    text = input().strip()
    print(BWT(text))