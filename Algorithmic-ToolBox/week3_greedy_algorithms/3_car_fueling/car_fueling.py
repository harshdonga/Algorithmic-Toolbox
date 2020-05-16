import sys
def compute_min_refills(distance, tank, stops):
    s = 0
    stops.append(distance)
    left = tank
    for i in range(len(stops)-1):
        if (left - stops[i]) > 0 and (left - stops[i+1]) >= 0:
            continue

        elif (left - stops[i]) >= 0 and (left - stops[i+1]) < 0 and (stops[i+1]-stops[i]) <= tank:
            s += 1
            left = tank + stops[i]
        else:
            return -1
    return s

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
