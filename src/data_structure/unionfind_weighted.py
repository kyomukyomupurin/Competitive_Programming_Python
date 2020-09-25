# Union Find Tree(weighted)
# verified by
#     https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_1_B

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n
        self.rank = [0] * n
        self.diff_weight = [0] * n

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            r = self.root(self.par[x])
            self.diff_weight[x] += self.diff_weight[self.par[x]]
            self.par[x] = r
            return self.par[x]

    def weight(self, x):
        self.root(x)
        return self.diff_weight[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    # y is w larger than x
    def unite(self, x, y, w):
        w += self.weight(x)
        w -= self.weight(y)
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
            w = -w
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x
        self.diff_weight[y] = w
        return

    def diff(self, x, y):
        return self.weight(y) - self.weight(x)

# verification code
"""
def DSL_1_B():
    n, q = map(int, input().split())
    uf = UnionFind(n)

    for i in range(q):
        query = list(map(int, input().split()))
        if len(query) == 3:
            x, y = int(query[1]), int(query[2])
            if uf.same(x, y):
                print(uf.diff(x, y))
            else:
                print('?')
        else:
            x, y, z = int(query[1]), int(query[2]), int(query[3])
            uf.unite(x, y, z)
"""