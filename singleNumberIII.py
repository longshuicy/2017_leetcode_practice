import collections
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct = collections.Counter(nums)
        for key in dct.keys():
            if dct[key]==1:
                return key

if __name__ == '__main__':
    test = Solution()
    test.singleNumber([1,1,1,2,3,3,3])
