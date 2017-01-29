class Solution(object):
    def sumDigits(self,n):
        summation = 0
        while(n>0):
            
            summation += (n%10)**2
            n /= 10
        return summation
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        square_sum = []
        
        if self.sumDigits(n) == 1:
            return True
        while n not in square_sum:
            if self.sumDigits(n) == 1:
                return True
            else:
                square_sum.append(n)
                n = self.sumDigits(n)
        return False

if __name__ == '__main__':
    test = Solution()
    print(test.isHappy(7))
