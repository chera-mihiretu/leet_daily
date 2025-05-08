class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        heap = []
        heappush(heap, [0,0,0,2]) # distance, r, c, last_move
        distance = [[float('inf') for i in range(len(moveTime[0]))] for j in range(len(moveTime))]
        distance[0][0] = 0
        visited = set()
        move = {1:2,2:1}
        def inbound(r, c):
            return 0 <= r < len(moveTime) and 0 <= c < len(moveTime[0])
        while heap:
            dist, r, c, last = heappop(heap)

            if (r,c) in visited:continue
            # print(distance)
            if (r,c) == (len(moveTime) - 1, len(moveTime[0]) - 1): return dist
            visited.add((r,c))

            for x, y in [(0,1),(0,-1),(1,0), (-1,0)]:
                next_r = x + r
                next_c = y + c
                if inbound(next_r, next_c):
                    next_dist = max(moveTime[next_r][next_c] + move[last],  dist + move[last])

                    if next_dist < distance[next_r][next_c]:
                        distance[next_r][next_c] = next_dist
                        heappush(heap, [next_dist, next_r, next_c, move[last]])
        return -1
                

            