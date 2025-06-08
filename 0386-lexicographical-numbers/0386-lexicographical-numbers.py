class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        answer = []
        def backtrack(k):
            nonlocal answer
            if k > n:
                return 
            answer.append(k)

            for i in range(10):
                if k == 0 and i == 0: continue 
                backtrack((k * 10) + i)
        backtrack(0)
        return answer[1:]
            

        