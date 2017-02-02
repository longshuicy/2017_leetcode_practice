class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # two pointer is just confusing.. try one pointer!
            
        # clean the array!
        while len(nums1)>m:
            nums1.pop()
        while len(nums2)>n:
            nums2.pop()
            
        if m == 0:
            nums1 += nums2
        
        else:
                
            i = 0
            while nums2 != [] and i<m+n:
                
                #print(nums1,nums2)
               
                if nums2[0] > nums1[i]:
                    if i == len(nums1)-1:
                        nums1 += nums2
                        i += len(nums2)+1
                        
                    else:
                        i += 1
                else:
                    nums1.insert(i,nums2[0])
                    nums2.pop(0)
                    i += 1

        return nums1

if __name__ == '__main__':
    test = Solution()
    print(test.merge([1,2,3,0,0,0],3,[2,5,6],3))
