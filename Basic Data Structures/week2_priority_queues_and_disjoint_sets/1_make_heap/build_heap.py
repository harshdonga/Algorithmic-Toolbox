# python3

class build_heap:
    def __init__(self, n, data):
        self.swaps = []
        self.data = data
        self.n = n


    def output(self):
        print(len(self.swaps))
        for swap in self.swaps:
            print(swap[0], swap[1])

    def do_swaps(self, i):
        if i != 0:
            x = int((i-1)/2)
            if self.data[x] > self.data[i]:
                self.swaps.append((x,i))
                self.data[x], self.data[i] = self.data[i] , self.data[x]
                self.do_swaps(x)
            

    def swapping(self):
        for i in range(self.n - 1, 0 ,-1):
            self.do_swaps(i)         


    def solve(self):
        self.swapping()
        self.output()

if __name__ == "__main__":
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    heap = build_heap(n, data)
    heap.solve()