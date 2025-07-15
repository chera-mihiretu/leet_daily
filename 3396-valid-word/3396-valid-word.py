class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False 
        vowels = {"A", "a", "e","E", 'I','i', 'o','O', 'u', "U"}
        cons = 0 
        vows = 0
        for i in word:
            if ord("a") <= ord(i) <= ord("z") or ord("A") <= ord(i) <= ord("Z"):
                if i not in vowels:
                    cons += 1
                else:
                    vows += 1
            if not ord("a") <= ord(i) <= ord("z") and not ord("A") <= ord(i) <= ord("Z") and not ord("0") <= ord(i) <= ord("9"):
                return False
        return min(vows, cons) > 0