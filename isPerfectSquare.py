class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        i = 1
        
        while num-i >= 0:
            num -= i
            i += 2
            
        if num == 0:
            return True
        else:
            return False

if __name__ =='__main__':
    test = Solution()
    print(test.isPerfectSquare(256))
