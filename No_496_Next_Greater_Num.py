class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def findGreater(number):
                for i in range(nums2.index(n1),len(nums2)):
                    if nums2[i] > n1:
                        return nums2[i]
                return -1
        
        output = []
        for n1 in nums1:
            output.append(findGreater(n1))
        return output
