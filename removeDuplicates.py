class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #print(nums)
        if not nums:
            return 0
        elif len(nums)==1:
            return 1
        
        i = 0
        while i < len(nums)-1:
            if nums[i]==nums[i+1]:
                nums.remove(nums[i])
            else:
                i += 1
            print(nums)
                
        return nums
                


if __name__ == '__main__':

    test = Solution()
    print(test.removeDuplicates([1,2,2,3]))
