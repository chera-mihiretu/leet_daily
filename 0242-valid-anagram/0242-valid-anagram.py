class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = [0 for i in range(26)]
        arr2 = [0 for i in range(26)]
        if len(s) != len(t):
            return False 
        def index(s):
            return ord(s) - ord('a')
        for i in range(len(s)):
            arr1[index(s[i])] += 1
            arr2[index(t[i])] += 1
        return arr1 == arr2