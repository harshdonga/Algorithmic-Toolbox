# python3

import sys

class Solver:
	def __init__(self, s):
		self.s = s
	def ask(self, a, b, l):
		if s[a] == s[b] and s[a+(l//2)] == s[b+(l//2)] and s[a+(l//5)] == s[b+(l//5)] and s[a+l-1] == s[b+l-1]:
			return s[a:a+l] == s[b:b+l]
		else:
			return False

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")