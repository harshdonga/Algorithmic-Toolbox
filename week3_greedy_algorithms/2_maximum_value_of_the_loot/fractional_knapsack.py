import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    x = 0
    l = []
    for i in range(len(values)):
        l.append(values[i]/weights[i])
   
    for i in range(len(values)):
        ind = l.index(max(l))
        if x + weights[ind] <= capacity:
            x += weights[ind]
            value += values[ind]
        else:
            value += values[ind]*(capacity- x)/weights[ind]
            x = capacity
            break
            
        l.pop(ind)
            
    
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))