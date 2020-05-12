# Uses python3
import sys

def get_majority_element(a,n):
    s = set(a)
    threshold = int(n/2) + 1
    if n %2 == 0:
        max_nums = threshold -1 
    else: 
        max_nums = threshold
    if len(s) > max_nums:
        return -1
    else:
        d = {}
        for i in a:
            i = str(i)
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for val in d.values():
            if val >= threshold:
                return 1
                break
        return -1
    
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a,len(a)) != -1:
        print(1)
    else:
        print(0)