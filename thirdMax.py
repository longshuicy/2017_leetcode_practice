class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sorted
        nums = sorted(nums,reverse= True)
        # remove duplication
        i = 0
        while i<len(nums)-1:
            #print(nums)
            
            if nums[i]==nums[i+1]:
                nums.remove(nums[i])
            else:
                i += 1
                
        #print(nums)
        
        if len(nums)>=3:
            return nums[2]
        else:
            return nums[0]


if __name__ == "__main__":
    test = Solution()
    print(test.thirdMax([1,4,35,2,3,5,82,32]))
