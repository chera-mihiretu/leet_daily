class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # a - b -> small means he should go to b
        # 
        ans = 0
        costs.sort(key=lambda x: x[0] - x[1])
        for i in range(len(costs)):
            ans += costs[i][int(i >= (len(costs)//2))]
        return ans

