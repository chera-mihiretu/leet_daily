class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = self.ppow(x, abs(n))

        if n > 0:
            return result
        return 1 / result

    def ppow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x

        result =  self.ppow(x, n//2)
        result *= result
        if n & 1:
            result *= x
        
        return result
