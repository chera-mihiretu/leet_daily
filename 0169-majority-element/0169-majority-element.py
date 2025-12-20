class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter={}
        for i in range(len(nums)):
            if nums[i] in counter:
                counter[nums[i]]+=1
            else:
                counter[nums[i]]=1
        for key,no in counter.items():
            if no>(len(nums)//2):
                return key




        