class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.insert(len(nums),i)

        print(nums)
            

if __name__ == '__main__':

    test = Solution()
    test.moveZeroes([0,1,2,0,4,7,0])

