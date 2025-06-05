class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)
        for i in range(len(s1)):
            c1 = ord(s1[i]) - ord("a")
            c2 = ord(s2[i]) - ord("a")
            uf.union(c1, c2)
        groups = defaultdict(list)
        for i in range(26):
            groups[uf.find(i)].append(i)
        mapper = {}
        for _, indices in groups.items():
            group_min = min(indices)
            for i in indices:
                mapper[i] = group_min
        string = []
        for c in baseStr:
            i = mapper[ord(c) - ord("a")]
            string.append(chr(ord("a") + i))
        return "".join(string)


class UnionFind:
    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]

    def find(self, node: int) -> int:
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, parent: int, node: int) -> None:
        root_parent = self.find(parent)
        root_node = self.find(node)
        if root_parent == root_node:
            return
        if self.rank[root_parent] > self.rank[root_node]:
            self.root[root_node] = root_parent
        elif self.rank[root_parent] < self.rank[root_node]:
            self.root[root_parent] = root_node
        else:
            self.root[root_node] = root_parent
            self.rank[root_parent] += 1