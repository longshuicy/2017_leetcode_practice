class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i =1
        
        while n >= i:
            
            n -= i
            i += 1
            
        return i-1

if __name__ == '__main__':
    test = Solution()
    print(test.arrangeCoins(10))
