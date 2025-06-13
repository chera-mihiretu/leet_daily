class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def check(mid):
            i = 1
            count = 0
            while i < len(nums):
                if abs(nums[i] - nums[i-1] ) <= mid:
                    count += 1
                    i += 1
                i  +=1
            return count

        start = 0
        end =  nums[-1] - nums[0]  
        answer = 0
        while start <= end:
            mid = (start + end) // 2 


            if check(mid) < p:
                start = mid + 1
            else:
                answer = mid
                end = mid - 1
        return start