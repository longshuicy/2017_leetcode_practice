import collections
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        freq = collections.Counter(nums)
        for key in freq.keys():
            if freq[key]>1:
                return True
                
        return False

if __name__ == '__main__':
    test = Solution()
    print(test.containsDuplicate([1,2,3,4,5,5,5,6]))
