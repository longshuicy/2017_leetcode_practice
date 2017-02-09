class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(range(1,10), k, n, 0, [], res)
        return res
    
    def dfs(self, nums, k, n, index, path, res):
        
        if k < 0 or n < 0: # backtracking 
            return 
        
        if k == 0 and n == 0: 
            res.append(path)
        
        for i in range(index, len(nums)):
            self.dfs(nums, k-1, n-nums[i], i+1, path+[nums[i]], res)


if __name__ =='__main__':

    test = Solution()
    print(test.combinationSum3(3,9))   
