class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = 1
        count = 9
        start = 1
        
        while n > digits*count:
            n -= digits*count
            digits += 1
            count *= 10
            start *= 10
            
        #print(start)
        start = start + (n - 1)/digits
        s = str(start)
        
        return int(s[(n - 1)%digits])
		

if __name__ == '__main__':

    test = Solution()
    print(test.findNthDigit(11))
