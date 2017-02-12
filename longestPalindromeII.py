class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # Create a table to store results of subproblems
        dp = [[1 for x in range(n)] for x in range(n)]
        
        #print(dp)
        for length in range(2,n+1):
            
            for i in range(n-length+1):
                j = i + length -1
                #If (X[i] != X[j])  L(i, j) =  max{L(i + 1, j),L(i, j - 1)}
                
                if s[i] != s[j]:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                # If there are only 2 characters and both are same Else if (j == i + 1) L(i, j) = 2 
                elif length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i+1][j-1] + 2
                # If there are more than two characters, and first and last 
                # characters are same
                #Else L(i, j) =  L(i + 1, j - 1) + 2 
                
                i += 1
        
        return dp[0][-1]

if __name__ == '__main__':
    test = Solution()
    print(test.longestPalindromeSubseq("abbcegbba")) 
