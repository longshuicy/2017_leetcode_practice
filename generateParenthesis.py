class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left,right, ans, "")
        
        return ans

    def dfs(self, left, right, ans, string):
        print(string,left, right)
        if right < left:
            return
            
        if not left and not right:
            ans.append(string)
            return
        if left:
            self.dfs(left-1, right, ans, string + "(")
        if right:
            self.dfs(left, right-1, ans, string + ")")

if __name__ == '__main__':
    test = Solution()
    print(test.generateParenthesis(2))
