import random
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        index = []
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                index.append(i)
        print(index)
        return random.choice(index)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

if __name__ == '__main__':
    test = Solution([1,2,1,2,1])
    print(test.pick(1))
    
