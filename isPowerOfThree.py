class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        '''if n == 0:
            return False
        else:

            if n%3==0 and n!=1:
                return self.isPowerOfThree(n/3)
            elif n==1:
                return True
            else:                
                return False'''
                

        # Could you do it without using any loop / recursion?
        maxPowerOfThree = 1162261467
        return (n>0 and maxPowerOfThree%n == 0)


if __name__ == '__main__':
    test= Solution()
    print(test.isPowerOfThree(81))
