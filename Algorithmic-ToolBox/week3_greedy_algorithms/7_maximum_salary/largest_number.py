import sys

def is_greater(n, m):
	n = str(n)
	m = str(m)
	return n+m > m+n
def largest_number(a):
    res = ''

    while len(a) > 0:
    	max_num = '0'
    	for num in a:
    		if is_greater(num, max_num):
    			max_num = num
    	res += max_num
    	a.pop(a.index(max_num))

    return ''.join(map(str, res))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))