class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        m = 0
        for i in range(len(nums)):
            m |= nums[i]
        
        def t(index, r):
            if index == len(nums):
                return int(r == m)
            
            return t(index + 1, r) + t(index + 1, r | nums[index])
        return t(0, 0)
