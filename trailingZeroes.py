import math
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 5
        count = 0
 
        while n/i>=1:
            count += int(n/i)
            i *= 5

        return count



if __name__ == '__main__':

    test = Solution()
    print(test.trailingZeroes(5))
