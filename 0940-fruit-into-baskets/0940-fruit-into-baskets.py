class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = Counter([fruits[0]])
        start = end = 0
        answer = 1
        while end < len(fruits):
            if len(count) <= 2:
                end += 1
                if end < len(fruits):
                    count[fruits[end]] += 1
            else:
                count[fruits[start]] -= 1
                if count[fruits[start]] == 0:
                    count.pop(fruits[start])
                start +=1 
            if end < len(fruits) and len(count) <= 2:
                answer = max(answer, count.total())
        return answer