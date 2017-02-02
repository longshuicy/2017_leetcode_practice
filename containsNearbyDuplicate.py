class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        # sliding window algorithm
        
        if len(nums)==0 or len(nums)==1:
            return False
        
        # too slow, using hashmap?
        
        '''for length in range(1, k+1):
            i = 0
            #print('length',length)
            
            while i+length <len(nums):
                #print(i)
                if nums[i] == nums[i+length]:
                    return True
                
                else:
                    i += 1
        
        return False'''
        
    
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
            
                
if __name__ =='__main__':
    test = Solution()
    print(test.containsNearbyDuplicate([1,2,1,3,5,3],3))
