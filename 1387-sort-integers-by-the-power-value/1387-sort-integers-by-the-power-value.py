class Solution:
    def __init__(self):
        self.memo = {}
    def getKth(self, lo: int, hi: int, k: int) -> int:
        arr = [i for i in range(lo, hi+1)]
        arr.sort(key=lambda x: self.getThePower(x))
        return arr[k-1]

    def getThePower(self, n):
        step = 0
        temp = n
        while temp != 1:
            if temp in self.memo:
                self.memo[n] = self.memo[temp] + step
                return self.memo[n]
            if temp & 1: temp = temp * 3 + 1
            else: temp //= 2
            step += 1
        self.memo[n] = step
        return step 