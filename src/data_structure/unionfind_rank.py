# Union Find Tree(rank)
# verified by
#     https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_1_A

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n
        self.rank = [0] * n

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x
        return

# verification code
"""
def DSL_1_A():
    n, q = map(int, input().split())
    uf = UnionFind(n)

    for i in range(q):
        t, u, v = map(int, input().split())

        if t:
            print(int(uf.same(u, v)))
        else:
            uf.unite(u, v)
"""