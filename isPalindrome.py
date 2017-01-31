class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x<0 or (x!=0 and x%10==0):
            return False
            
        # reverse algorithm
        sum = 0
        
        while x>sum:
            sum = sum*10 + x%10
            x = int(x/10)
            #print(x,sum)
            
        if sum == x or x == int(sum/10):
            return True
        else:
            return False


if __name__ == '__main__':

    test = Solution()
    print(test.isPalindrome(515))
