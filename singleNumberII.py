import collections
import operator

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dct = collections.Counter(nums)
        sorted_dct = sorted(dct.items(), key=operator.itemgetter(1))
        
        #print(sorted_dct)
        
        return [sorted_dct[0][0],sorted_dct[1][0]]

if __name__ == '__main__':
    test = Solution()
    print(test.singleNumber([1,2,3,3,4,4]))


# slow, can work faster!
