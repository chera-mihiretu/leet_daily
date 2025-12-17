class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0 for i in range(n)]
        right = [0 for j in range(n)]

        for i in range(n):
            left[i] = max(left[i-1], height[i])
        for j in range(n-1,-1,-1):
            right[j] = max(right[(j + 1) % n], height[j])
        
        answer = 0
        for i in range(n):
            answer += max(0,min(left[i], right[i]) - height[i])
        return answer