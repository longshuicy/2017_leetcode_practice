class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        
        while i <len(nums):
            
            if target == nums[i]:
                return i
            elif target > nums[i]:
                i += 1
            else:
                return i
        
        return len(nums)

if __name__ == '__main__':

    test = Solution()
    print(test.searchInsert([1],2))
