# Segment Tree
# non-recursive version
# verified by
#     https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_A
#     https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_2_B

class SegmentTree:
    def __init__(self, data : list, ie, f):
        self.data = data
        self.ie = ie
        self.f = f
        self.sz = len(self.data)
        self.n = 1

        while self.n < self.sz:
            self.n <<= 1

        self.node = [ie] * (2 * self.n)

        for i in range(self.sz):
            self.node[i + self.n] = self.data[i]

        for i in range(self.n - 1, 0, -1):
            self.node[i] = self.f(self.node[2 * i], self.node[2 * i + 1])

    def update(self, pos : int, val):
        pos += self.n
        self.node[pos] = val
        while pos:
            pos >>= 1
            self.node[pos] = self.f(self.node[2 * pos], self.node[2 * pos + 1])

    def get(self, l : int, r : int):
        vl, vr = self.ie, self.ie
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                vl = self.f(vl, self.node[l])
                l += 1
            if r & 1:
                r -= 1
                vr = self.f(self.node[r], vr)
            l >>= 1
            r >>= 1
        return self.f(vl, vr)

    def at(self, pos : int):
        return self.node[self.n + pos]

# verification code
"""
def DSL_2_A():
    n, q = map(int, input().split())

    data = [2**31 - 1] * n
    ie = 2**31 - 1
    f = lambda x, y: min(x, y)

    seg = SegmentTree(data, ie, f)

    for i in range(q):
        com, x, y = map(int, input().split())

        if com:
            print(seg.get(x, y + 1))
        else:
            seg.update(x, y)
"""

"""
def DSL_2_B():
    n, q = map(int, input().split())

    data = [0] * n
    ie = 0
    f = lambda x, y: x + y

    seg = SegmentTree(data, ie, f)

    for i in range(q):
        com, x, y = map(int, input().split())

        if com:
            x -= 1
            y -= 1
            print(seg.get(x, y + 1))
        else:
            x -= 1
            seg.update(x, seg.at(x) + y)
"""