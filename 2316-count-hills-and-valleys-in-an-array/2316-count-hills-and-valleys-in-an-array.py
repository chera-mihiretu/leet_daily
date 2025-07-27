class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        back = []
        answer = 0
        for i in range(len(nums)):
            if back and back[-1] != nums[i]:
                back.append(nums[i])
            elif not back:
                back.append(nums[i])
        print(back)
        for i in range(1, len(back) - 1):
            if max(back[i-1], back[i], back[i+1]) == back[i]:
                answer += 1
            elif min(back[i-1], back[i], back[i+1]) == back[i]:
                answer += 1
        return answer
