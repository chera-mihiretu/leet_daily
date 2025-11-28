class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = self.ppow(x, abs(n))

        if n > 0:
            return result
        return 1 / result

    def ppow(self, x, n):
        result = 1
        while (n > 0):
            if (n & 1):result *= x
            x *= x
            n >>= 1
        return result

        """
        
        3 ^ (7) -> 3 ^ (4 + 2 + 1) 

        3^4 * 3^2 * 3^1

        7-> 111

        2 
        3 * 3 * 9 


        
        
        """
