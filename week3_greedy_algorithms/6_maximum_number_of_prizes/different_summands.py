# Uses python3
import sys

def optimal_summands(n):
    summands = []
    x = 0
    incr = 1
    while x <= n:
        if x + incr <= n:
            summands.append(incr)
            x = x + incr
        else:
            break
        incr += 1
    summands.pop(-1)
    summands.append(n-sum(summands))
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
