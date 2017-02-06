# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #for v in range(1,n+1):
        #    if isBadVersion(v) is True:
        #        return v
        # too slow O(n)
        
        # binary search
        left = 1
        right = n
        
        while left < right:
            mid = int((left+ right)/2)
            if isBadVersion(mid) == True:
                right = mid
            else:
                left = mid+1
                
        return left
                
                
