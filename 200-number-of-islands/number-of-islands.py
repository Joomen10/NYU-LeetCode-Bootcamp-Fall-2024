class Solution:
    def numIslands(self, grid):


        if not grid:
            return 0

        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i , j)
                    num_islands += 1
        
        return num_islands

    def dfs(self, grid, r, c):
        if (
            r < 0
            or c < 0
            or r >= len(grid)
            or c >= len(grid[0])
            or grid[r][c] != "1"
        ):
            return
        grid[r][c] = "0"

        self.dfs(grid, r-1, c)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r, c+1)



    # if not grid:
    #     return 0

    # nr = len(grid)
    # nc = len(grid[0])
    # nums_islands = 0

    # for r in range(nr):
    #     for c i range(nc):
    #         if gird[r][c] == "1":
    #             num_islands += 1
    #             grid[r][c] = 0
    #             neighbors = []
    #             neighbors.append((r,c_))

    #             while neighbors:
    #                 row, col = neighbors.pop(0)
    #                 if row - 1 >= 0 and grid[row - 1][col] == "1":


        
        