class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            temp = nums.pop()
            #print(temp)
            
            nums.insert(0,temp)
            k -= 1

        return nums

if __name__ == '__main__':
    test = Solution()
    print(test.rotate([1,2,3,4,5],4))
