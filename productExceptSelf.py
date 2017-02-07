class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #left to me, right to me
        
        multiply = []
        p = 1
        for num in nums:
            multiply.append(p)
            p *= num
        #print(multiply)
        
        p =1
        for i in range(len(nums)):
            multiply[len(nums)-i-1] *= p
            p *= nums[len(nums)-i-1]
            
        
        return multiply

if __name__ == '__main__':
    test = Solution()
    print(test.productExceptSelf([1,2,3,4,5]))
