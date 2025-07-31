class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        cur = {0}

        for i in arr:
            cur = {i | x for x in cur} | {i}
            ans |= cur
        return len(ans)