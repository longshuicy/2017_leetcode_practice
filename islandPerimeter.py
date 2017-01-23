class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # naive approach
        # side, corner and middle
        preim = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col] == 1:
                    if row +1 <= len(grid) -1:
                        preim += 1-grid[row+1][col]
                    elif row  == len(grid) -1:
                        preim += 1
                    
                    if row -1 >= 0:
                        preim += 1-grid[row-1][col]
                    elif row == 0:
                        preim += 1
                   
                    if col +1 <= len(grid[row])-1:
                        preim += 1-grid[row][col +1]
                        #print(preim)
                    elif col  == len(grid[row])-1:
                        preim += 1
                        
                    if col-1 >= 0:
                        preim += 1-grid[row][col-1]
                    elif col == 0:
                        preim += 1
                        
                #print(row,col,preim)
        
        #print(preim)
        
        return preim


if __name__ == "__main__":
    grid = [[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]
    test = Solution()
    print(test.islandPerimeter(grid))
