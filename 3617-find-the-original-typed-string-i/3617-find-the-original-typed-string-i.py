class Solution:
    def possibleStringCount(self, word: str) -> int:
        answer = 1
        for i in range(1, len(word)):
            answer += word[i] == word[i-1]
        return answer