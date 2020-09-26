# Fenwick Tree(Binary Indexed Tree) (for range add query)
# verified by 
#     https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_G

class FenwickTreeRAQ:
    def __init__(self, data : list):
        self.data = data
        self.n = len(data)
        self.ft1 = FenwickTree(data)
        self.ft2 = FenwickTree(data)

    def _add(self, ft : FenwickTree, l : int, r : int, val : int):
        ft.add(l, val)
        ft.add(r, -val)

    # add val range [l, r)
    def add(self, l : int, r : int, val : int):
        self._add(self.ft1, l, r, val)
        self._add(self.ft2, l, r, -val * (l - 1))
        self._add(self.ft2, r, n, val * (r - l))

    # get sum of [0, i]
    def _get(self, pos : int) -> int:
        return self.ft1.get(0, pos + 1) * pos + self.ft2.get(0, pos + 1)

    # get sum of [l, r]
    def get(self, l : int, r : int) -> int:
        return self._get(r) - self._get(l - 1)

# verification code
"""
def DSL_2_G():
    n, q = map(int, input().split())

    data = [0] * n
    ft = FenwickTreeRAQ(data)

    for i in range(q):
        l = list(map(int, input().split()))
        if len(l) == 3:
            s, t = l[1], l[2]
            s -= 1
            t -= 1
            print(ft.get(s, t))
        else:
            s, t, x = l[1], l[2], l[3]
            ft.add(s - 1, t, x)
"""