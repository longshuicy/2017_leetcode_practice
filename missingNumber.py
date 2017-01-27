class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sum of 0..n minus sum of the given numbers is the missing one.
        tot = 0
        for i in range(0,len(nums)+1):
            tot += i
            
        return tot - sum(nums)


if __name__ == '__main__':
    test = Solution()
    print(test.missingNumber([0,2,3,4,5,6]))
