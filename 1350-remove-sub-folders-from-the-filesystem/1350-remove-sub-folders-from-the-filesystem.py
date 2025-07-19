class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda x: len(x))
        s = set()
        for f in folder:
            exist = False
            for i in range(1, len(f)):
                if f[i] == '/':
                    if f[:i] in s:
                        exist = True
            if not exist:
                s.add(f)
        return list(s)