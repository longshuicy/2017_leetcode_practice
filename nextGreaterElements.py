class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # too slow
        ans = [-1] * len(nums)
        n = len(nums)
        stack = []
        nums *= 2
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                top = stack.pop()
                if top < n:
                    ans[top] = num
            stack.append(i)
        return ans
        
        # i dont understand!!

if __name__ =='__main__':

    test = Solution()
    print(test.nextGreaterElements([1,2,1]))                
