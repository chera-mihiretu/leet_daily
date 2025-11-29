class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [[-nums[i], i] for i in range(k)]
        heapify(heap)
        answer = [-heap[0][0]]
        start = 1
        for i in range(k, len(nums)):
            heappush(heap, [-nums[i], i])
            while heap[0][1] < start:
                heappop(heap)
            start += 1
            answer.append(-heap[0][0])
        return answer
            


