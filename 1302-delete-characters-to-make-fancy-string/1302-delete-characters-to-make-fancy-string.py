class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 0
        prev = "*"
        answer = ""
        for i in range(len(s)):
            if len(answer) >= 2:
                # print(answer)
                if answer[-1] == s[i] and answer[-2] == s[i]:
                    continue
           
            answer += s[i]
        return answer
        
            
            