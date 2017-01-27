class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        cnt = 0
        for num in nums:
            if num ==1:
                cnt += 1
                count = max(cnt,count)
            else:
                cnt = 0 
       
        return count

if __name__ == '__main__':
    nums = [1,1,1,1,0,1]
    test = Solution()
    print(test.findMaxConsecutiveOnes(nums))
