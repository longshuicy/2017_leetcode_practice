class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
            
        if x> 0:
            sum = 0
            while x>=1:
                sum = sum*10 + x%10
                x = int(x/10)
            
            if sum < 2**31:
                return sum
            else:
                return 0
            
        if x<0:
            sum = 0
            while abs(x)>=1:
                sum = sum*10 + abs(x)%10
                x = int(abs(x)/10)
            
            if sum < 2**31:
                return -1*sum
            else:
                return 0
            
if __name__ == '__main__':
    test = Solution()
    print(test.reverse(-1234534))
