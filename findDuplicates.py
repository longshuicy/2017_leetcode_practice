class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        twice = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                twice.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        
        return twice

if __name__ == '__main__':
    test = Solution()
    print(test.findDuplicates([1,1,2,2,3,6,5,5]))

