class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summation = nums[0]
        maximum = nums[0]
        
        for item in nums[1:]:
            if summation + item> item:
                summation = summation + item
            else: 
                summation = item
                
            maximum = max(summation, maximum)
            #print(summation,maximum)
            
        return maximum

if __name__ == '__main__':
    test = Solution()
    print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
