class Solution(object):
    def combinationSum4(self, nums, target):

        # recursive

        '''if target == 0:
          return 1

        count = 0
        for i in range(len(nums)):
            if target >= nums[i]:
                count += self.combinationSum4(nums,target - nums[i])

        return count'''

        # top down dp
        '''dp = [-1]*(target+1)
        dp[0] = 1

        def helper(nums,target):
            if dp[target]!= -1:
                return dp[target]

            count = 0
            for i in range(len(nums)):
                if target >= nums[i]:
                    count += helper(nums,target-nums[i])

            dp[target] = count
            #print(dp)
            return count


        return helper(nums,target)'''

        # bottom up dp
        dp = [0]*(target+1)
        dp[0] = 1

        for tg in range(1,len(dp)):
            for j in range(len(nums)):
                if tg - nums[j] >=0:
                    dp[tg] += dp[tg-nums[j]]
                print(dp)

        return dp[-1]

    
    

if __name__ == '__main__':
    test = Solution()
    print(test.combinationSum4([1,2,3],4))
