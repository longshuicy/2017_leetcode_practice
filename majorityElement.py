import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        freq = collections.Counter(nums)   
        for i in nums:
            if freq[i] > len(nums)/2:
                return i

if __name__ == '__main__':
    test = Solution()
    print(test.majorityElement([1,2,3,3,3,3]))
