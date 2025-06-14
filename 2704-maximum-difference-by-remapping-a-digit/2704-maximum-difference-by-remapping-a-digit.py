class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = list(str(num))
        change = '-1'
        small = []
        big = []
        for i in range(len(s)):
            if s[i] != '0':
                if change == '-1':
                    change = s[i]
                
                if change == s[i]:
                    small.append('0')
                else:
                    small.append(s[i])
            else:
                small.append(s[i])
        change = '-1'
        for i in range(len(s)):
            if s[i] != '9':
                if change == '-1':
                    change = s[i]
                if change == s[i]:
                    big.append('9')
                else:
                    big.append(s[i])
            else:
                big.append(s[i])

        return int(''.join(big)) - int(''.join(small))
