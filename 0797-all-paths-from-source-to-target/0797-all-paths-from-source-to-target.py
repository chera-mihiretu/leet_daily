class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        visited = set()

        def dfs(node, path):
            path.append(node)
            if node == len(graph) - 1:
                answer.append(path.copy())
                path.pop()
                return 

            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, path)
                    visited.discard(child)
            path.pop()
        dfs(0, [])
        return answer