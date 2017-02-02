class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        include = 0
        exclude = 0
        
        i = 0
        while i<len(nums):
            tmp = include
            include = nums[i] + exclude
            exclude = max(tmp, exclude)
            i += 1
        
            
            
        return max(include, exclude)


if __name__ == '__main__':

    test = Solution()
    print(test.rob([2,1,1,2]))

'''For every house k, there are two options: either to rob it (include this house: i) or not rob it (exclude this house: e).

Include this house:
i = num[k] + e (money of this house + money robbed excluding the previous house)

Exclude this house:
e = max(i, e) (max of money robbed including the previous house or money robbed excluding the previous house)
(note that i and e of the previous step, that's why we use tmp here to store the previous i when calculating e, to make O(1) space)
'''
