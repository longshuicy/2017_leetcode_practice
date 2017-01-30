class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0 
        while i < len(nums):
            #print(i)
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i += 1
                
        return nums
        
        
        # the trick is when you remove an item in the list,
        # the index <b>automatically</b> add one!

if __name__ == '__main__':

    test = Solution()
    print(test.removeElement([3,5,2,3,3],3))
