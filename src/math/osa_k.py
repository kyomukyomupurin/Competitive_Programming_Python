class osa_k:
    def __init__(self, n: int):
        self.n = n
        self.min_factor = [0] * (n + 1)
        self.pr = []

        for i in range(2, n + 1, 1):
            if not self.min_factor[i]:
                self.min_factor[i] = i
                self.pr.append(i)

            j = 0
            while (1):
                if j >= len(self.pr) or self.pr[j] > self.min_factor[i] or i * self.pr[j] > n:
                    break
                self.min_factor[i * self.pr[j]] = self.pr[j]
                j += 1

    def prime_factor(self, n : int) -> list :
        res = []
        while n != 1:
            p = self.min_factor[n]
            cnt = 0
            while self.min_factor[n] == p:
                cnt += 1
                n //= p
            res.append((p, cnt))
        return res