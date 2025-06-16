class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        answer = float('-inf')
        pre = nums[0]
        for i in range(1, len(nums)):
            answer = max(nums[i] - pre, answer)
            pre = min(nums[i], pre)
        return -1 if answer <= 0 else answer
