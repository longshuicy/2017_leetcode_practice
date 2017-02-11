class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return nums[i]'''
        
       
        low = 0
        high = len(nums)-1
        
        while low<high:
            mid = (low + high)/2
            count = 0
             
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            
            if count > mid:
                high = mid
            else:
                low = mid +1
        return low
                
 
if __name__ == '__main__':
    test = Solution()
    print(test.findDuplicate([1,2,3,4,5,6,7,7,8]))                   
