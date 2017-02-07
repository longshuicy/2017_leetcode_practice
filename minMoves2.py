class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # find the middle point and add all the difference to that
        mid = sorted(nums)[int(len(nums) / 2)]
        
        count = 0
        for i in nums:
            count += abs(i - mid)
            
        return count

if __name__ == '__main__':
    test = Solution()
    print(test.minMoves2([1,2,3]))
