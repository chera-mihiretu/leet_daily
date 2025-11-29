class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        n = len(equations)
        answer = []
        for i in range(n):
            # if equations[i][0] not in graph:
            #     graph[equations[i][0]] = []
            graph[equations[i][0]].append([equations[i][1], values[i]])
            # if equations[i][1] not in graph:
            #     graph[equations[i][1]] = []
            graph[equations[i][1]].append([equations[i][0], 1/values[i]])
        def dfs(node, target, visited):
            if node not in graph:
                return -1 
            if node == target:
                return 1 
            result = -1
            visited.add(node)
            for child, weight in graph[node]:
                if (child not in visited):
                    c = dfs(child, target, visited)
                    if c != -1:
                        return c * weight

            return result
        
        for a, b in queries:
            answer.append(dfs(a, b, set()))
        return answer