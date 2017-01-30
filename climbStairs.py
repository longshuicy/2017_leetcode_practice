class Solution(object):
    def climbStairs_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # fibonacci
        if n == 0:
            return 0
        if n ==1:
            return 1
        if n ==2:
            return 2
            
        i = 2
        n_1 = 2
        n_2 = 1
        sum = 0 
        while i < n:
            sum = n_1 + n_2
            n_2 = n_1
            n_1 = sum
            i = i+1
            
        return sum


    def climbStairs_2(self,n):
        # recursive algorithm takes way too long 
        if n == 0:
            return 0
        if n ==1:
            return 1
        if n ==2:
            return 2

        return self.climbStairs_2(n-1)+self.climbStairs_2(n-2)


if __name__ == '__main__':

    test = Solution()
    print(test.climbStairs_1(35))
    print(test.climbStairs_2(35))
