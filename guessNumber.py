# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
import math
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        begin = 1
        end = n
        
        while begin < end:
            mid = int((begin + end)/2)
            if self.guess(mid) == 1:
                begin = mid+1
            
            elif self.guess(mid) == -1:
                end = mid
            
            else:
                return mid
        
        return begin

