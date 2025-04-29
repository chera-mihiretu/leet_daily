
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        max_val = max(nums)
        max_count = 0
        start = 0
        for i in range(len(nums)):
            if nums[i] == max_val:
                max_count += 1
            while max_count == k:
                ans += len(nums) -  i
                if nums[start] == max_val:
                    max_count -= 1
                start += 1
        return ans
