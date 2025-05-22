class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        op = 0
        last = [0 for _ in range(len(nums) + 1)]
        heap = []
        j = 0
        for i in range(len(nums)):
            op += last[i]
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1
            
            while op < nums[i] and heap and -heap[0] >= i:
                op += 1
                last[-heap[0] + 1] -= 1
                heappop(heap)
            
            
            if op < nums[i]: return -1

        return len(heap)

                
