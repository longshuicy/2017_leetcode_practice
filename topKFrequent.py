import collections
import operator
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        dct = collections.Counter(nums)
        sorted_dct = sorted(dct.items(), key=operator.itemgetter(1), reverse = True) 
        
        frequent = []
        i = 0
        
        while i<k:
            frequent.append(sorted_dct[i][0])
            i += 1
            
        return frequent


if __name__ == '__main__':
    test = Solution()
    print(test.topKFrequent([4,4,4,4,5,5,5,5,5,1,2,1,1,2,1,1],3))
