# Fenwick Tree(Binary Indexed Tree) (for point add query)
# verified by 
#     https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_B

class FenwickTree:
    def __init__(self, data):
        self.data = data
        self.n = len(data) + 1
        self.node = [0] * (self.n + 1)

        for i in range(self.n - 1):
            self.add(i, self.data[i])

    def add(self, pos, val):
        pos += 1
        while pos < self.n:
            self.node[pos] += val
            pos += pos & -pos

    # return sum of [l, r)
    def get(self, l, r):
        res = 0

        while (l < r):
            res += self.node[r]
            r -= r & -r
        while r < l:
            res -= self.node[l]
            l -= l & -l

        return res

    def lower_bound(self, val):
        if val <= 0:
            return 0
        pos = 0
        k = 1

        while k < self.n - 1:
            k <<= 1
        while k > 0:
            if pos + k <= self.n - 1 and self.node[pos + k] < val:
                val -= self.node[pos + k]
                pos += k
            k >>= 1

        return pos

# verification code
"""
def DSL_2_B():
    n, q = map(int, input().split())
    data = [0] * n
    ft = FenwickTree(data)

    for i in range(q):
        com, x, y = map(int, input().split())
        if com:
            print(ft.get(x - 1, y))
        else:
            ft.add(x - 1, y)
"""