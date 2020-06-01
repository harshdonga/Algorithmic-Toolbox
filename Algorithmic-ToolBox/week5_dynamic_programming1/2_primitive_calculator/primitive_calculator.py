def optimal_sequence(n):
    dp_table = [0, 0] + [n+1]*(n-1)
    for i in range(2, n+1):
	temp1, temp2, temp3 = [n+1]*3
	temp1 = dp_table[i-1] + 1 
	if i%2 == 0: temp2 = dp_table[i//2] + 1
	if i%3 == 0: temp3 = dp_table[i//3] + 1
	min_ops = min(temp1, temp2, temp3)
	dp_table[i] = min_ops
    print(dp_table[n])
    sequence = [n]
    while n!=1:
	if n%3 ==0 and dp_table[n]-1 == dp_table[n//3]:
	    sequence += [n//3]
	    n = n//3
	elif n%2 ==0 and dp_table[n]-1 == dp_table[n//2]:
	    sequence += [n//2]
	    n = n//2
	else:
	    sequence += [n-1]
	    n = n - 1
    return reversed(sequence)

n = int(input())
sequence = list(optimal_sequence(n))
for x in sequence:
    print(x, end=' ')

