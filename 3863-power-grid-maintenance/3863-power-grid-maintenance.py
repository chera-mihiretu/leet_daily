class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = [i for i in range(c)]
        enabled = [True for i in range(c)]
        answer = []
        def union(x, y):
            parent[find(x)] = find(y)
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        for fr, to  in connections:
            union(fr - 1, to - 1)
        
        alive_mins = defaultdict(list)
        for i in range(c):
            fam = find(i)

            heappush(alive_mins[fam], i)
        
        for com, t in queries:
            if com == 1:
                if enabled[t-1]:
                    answer.append(t)
                    continue


                fam = find(t - 1)

                while alive_mins[fam] and (not enabled[alive_mins[fam][0]]):
                    heappop(alive_mins[fam])
                if alive_mins[fam]:
                    answer.append(alive_mins[fam][0] + 1)
                else:
                    answer.append(-1)
            else:
                enabled[t-1] = False
        return answer

