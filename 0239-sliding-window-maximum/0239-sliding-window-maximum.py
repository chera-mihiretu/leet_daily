class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        answer = []
        start = 0
        for i in range(len(nums)):
            
            while que and nums[que[-1]] < nums[i]:
                que.pop()
            que.append(i)

            if que and que[0] < start:
                que.popleft()
            if i - start + 1 == k:
                answer.append(nums[que[0]])

            if i - start + 1 == k:
                start += 1
        return answer
            



