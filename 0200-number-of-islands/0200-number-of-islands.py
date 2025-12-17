class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.dirs = [[-1,0], [1,0], [0,1],[0,-1]]
        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == "1":
                    count += 1
                    self.removeAllLand(i,j)
        return count

    def inbound(self, x, y):
        return 0 <= x < len(self.grid) and 0 <= y <len(self.grid[0])

    def removeAllLand(self, x, y):
        if self.grid[x][y] == "0":
            return
        self.grid[x][y] = "0"

        for h, v in self.dirs:
            new_x = x + h
            new_y = y + v
            if self.inbound(new_x, new_y):
                self.removeAllLand(new_x, new_y)
        


