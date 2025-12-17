class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        visited = set()

        def dfs(node, path):
            if node == len(graph) - 1:
                answer.append(path.copy())
                return 

            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    path.append(child)
                    dfs(child, path)
                    path.pop()
                    visited.discard(child)
        dfs(0, [0])
        return answer