class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # use XOR
        
        for num in nums[1:]:
            nums[0] = nums[0]^num
            #print(nums[0])
            
        return nums[0]

if __name__ == "__main__":
    test = Solution()
    print(test.singleNumber([1,1,3,4,4,2,2]))
