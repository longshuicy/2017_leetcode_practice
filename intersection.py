class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        return list(nums1&nums2)

if __name__ =='__main__':

    test = Solution()
    print(test.intersection([2,3,4,4],[2,4,5]))
