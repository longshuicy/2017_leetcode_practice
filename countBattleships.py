class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if len(board) == 0: return 0
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    # left and below should be empty to define a battle ship
                    
                    count += 1
        return count

if __name__ == '__main__':

    test = Solution()
    print(test.countBattleships(["X..X","...X","...X"]))
